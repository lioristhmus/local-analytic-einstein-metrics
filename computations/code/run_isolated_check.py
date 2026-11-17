"""Foreground mathematical-job controller; no mathematical processing on host."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import selectors
import subprocess as sp
import time

ap = argparse.ArgumentParser()
ap.add_argument('--max-r',type=int,choices=(1,2,3),required=True)
args = ap.parse_args()
base = Path(__file__).resolve().parent
lock = Path('/Users/studio/.local/state/math-job.lock')
name = 'einstein-exact-set-r%d-%d' % (args.max_r,os.getpid())
try:
    lock.mkdir()
except FileExistsError:
    raise SystemExit('MATH_LOCK_BUSY: no job started')
owner = {'executor':'codex:'+os.environ.get('CODEX_THREAD_ID','unknown'),
         'started_at':dt.datetime.now(dt.timezone.utc).isoformat(),
         'job_name':name}
(lock/'owner').write_text(json.dumps(owner)+'\n')
cid = None
confirmed_stopped = False
def docker(*a,timeout=15):
    return sp.run(['docker',*a],capture_output=True,text=True,timeout=timeout,check=True).stdout
try:
    info=json.loads(docker('info','--format','{{json .}}'))
    if not info.get('MemoryLimit') or not info.get('SwapLimit') or info.get('MemTotal',0)<4_000_000_000:
        raise RuntimeError('UNVERIFIED_VM_LIMITS')
    names=docker('ps','--format','{{.Names}}').splitlines()
    if set(names)-{'open-webui','caddy','redis','searxng'}:
        raise RuntimeError('OTHER_RUNNING_CONTAINER_REQUIRES_REVIEW: '+','.join(names))
    service_usage=docker('stats','--no-stream','--format','{{.Name}} {{.CPUPerc}} {{.MemUsage}}')
    cmd=['create','--name',name,'--network=none','--cpus=1',
         '--memory=1900m','--memory-swap=1900m','--pids-limit=64',
         '--restart=no','--read-only','--cap-drop=ALL',
         '--security-opt=no-new-privileges','--ipc=none',
         '--tmpfs','/tmp:rw,size=33554432',
         '--env','DOT_SAGE=/tmp/dot_sage','--env','MPLCONFIGDIR=/tmp/matplotlib',
         '--workdir','/tmp',
         '--ulimit','fsize=16777216:16777216','--ulimit','nofile=128:128',
         '--log-driver=local','--log-opt','max-size=1m','--log-opt','max-file=2',
         '--mount','type=bind,src='+str(base)+',dst=/job,readonly',
         '--entrypoint','/usr/bin/timeout','sagemath/sagemath:10.9',
         '--signal=TERM','--kill-after=5s','880s','sage','-python',
         '/job/check_kasner_recursion.py','--max-r',str(args.max_r)]
    cid=docker(*cmd).strip()
    owner['container_id']=cid
    (lock/'owner').write_text(json.dumps(owner)+'\n')
    cfg=json.loads(docker('inspect',cid))[0]
    h=cfg['HostConfig']
    assert 0<h['Memory']<=2_000_000_000 and h['MemorySwap']==h['Memory']
    assert h['NanoCpus']==1_000_000_000 and h['NetworkMode']=='none'
    assert h['PidsLimit']==64 and h['RestartPolicy']['Name']=='no'
    assert h['ReadonlyRootfs'] and not h.get('OomKillDisable',False)
    # Docker create does not run the workload. All verified limits precede start.
    begun=time.monotonic()
    proc=sp.Popen(['docker','start','--attach',cid],stdout=sp.PIPE,stderr=sp.STDOUT)
    sel=selectors.DefaultSelector()
    sel.register(proc.stdout,selectors.EVENT_READ)
    output=bytearray()
    timed_out=False
    while proc.poll() is None or sel.get_map():
        if time.monotonic()-begun>895:
            timed_out=True
            docker('kill',cid)
            break
        events=sel.select(timeout=1)
        for key,_ in events:
            part=os.read(key.fd,4096)
            if not part:
                sel.unregister(key.fileobj)
            else:
                output.extend(part)
                if len(output)>65536:
                    docker('kill',cid)
                    raise RuntimeError('HOST_OUTPUT_BOUND')
    proc.wait(timeout=10)
    state=json.loads(docker('inspect','--format','{{json .State}}',cid))
    if state['Running']:
        docker('kill',cid)
        state=json.loads(docker('inspect','--format','{{json .State}}',cid))
    confirmed_stopped=not state['Running']
    result={'controller_status':'STOPPED' if confirmed_stopped else 'UNKNOWN',
            'container_id':cid,'image_id':cfg['Image'],'limits':{
            'memory_bytes':h['Memory'],'memory_plus_swap_bytes':h['MemorySwap'],
            'nano_cpus':h['NanoCpus'],'network':h['NetworkMode'],
            'pids':h['PidsLimit'],'restart':h['RestartPolicy']['Name'],
            'inner_wall_limit_seconds':880,'outer_wall_limit_seconds':895,
            'log':h['LogConfig'],'tmpfs':h['Tmpfs'],'read_only':h['ReadonlyRootfs']},
            'vm':{'memory_bytes':info['MemTotal'],'cpu_count':info['NCPU']},
            'existing_service_usage':service_usage,
            'exit_code':state['ExitCode'],'oom_killed':state['OOMKilled'],
            'timed_out':timed_out,'wall_seconds':time.monotonic()-begun,
            'output':output.decode('utf-8',errors='replace')}
    dest=base/('kasner-r%d-result.json'%args.max_r)
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(dest),'exit_code':state['ExitCode'],
                      'oom_killed':state['OOMKilled'],'timed_out':timed_out,
                      'output':result['output']}))
    if not confirmed_stopped or state['ExitCode'] or state['OOMKilled'] or timed_out:
        raise RuntimeError('CHECK_DID_NOT_PASS')
finally:
    if cid:
        try:
            st=json.loads(docker('inspect','--format','{{json .State}}',cid))
            if st['Running']:
                docker('kill',cid)
                st=json.loads(docker('inspect','--format','{{json .State}}',cid))
            if not st['Running']:
                confirmed_stopped=True
                docker('rm',cid)
        except Exception:
            pass
    else:
        confirmed_stopped=True
    if confirmed_stopped:
        (lock/'owner').unlink()
        lock.rmdir()
