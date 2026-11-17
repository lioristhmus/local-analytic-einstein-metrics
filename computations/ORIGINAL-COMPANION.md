# Exact Kasner recurrence check

The companion archive, [exact-set-checks-v0.1.1.zip](../paper/exact-set-checks-v0.1.1.zip), contains the SageMath program, the isolated foreground controller and the recorded exact results for orders 1 and 3. Its `SHA256SUMS.json` identifies every supplied file.

## Mathematical inputs and conventions

The metric is `dt^2 - sum(t^(2*p_i) dx_i^2)` with exponents `(-2/7, 3/7, 6/7)`, at `t=1`, and Einstein coefficient zero. In the orthonormal frame, `eta=diag(1,-1,-1,-1)`, the nonzero connection coefficients are `Gamma[i,0,i]=Gamma[i,i,0]=p_i/t`, and `[e_0,e_i]=-(p_i/t)e_i`. The curvature convention is `R(a,b)=[nabla_a,nabla_b]-nabla_[a,b]`, with the output lowered in the last slot. Every derivative slot receives its connection action.

The normalized spin tangent basis is given by the columns of `L/sqrt(2)`, ordered `00',01',10',11'`, where

```text
L = [1   0    0   1]
    [0   1    1   0]
    [0  -i    i   0]
    [1   0    0  -1].
```

The implementation uses `L` itself, so all arithmetic lies in the rational Gaussian field `Q(i)`. A covariant tensor of rank `r+4` acquires the common factor `2^((r+4)/2)`. The two sides of each tested order-r Spencer identity acquire the same factor of rank `r+5`, which cancels. The alternating matrices and Weyl extraction signs match §2 of the paper.

The geometric route computes ordered curvature derivatives through order four, symmetrizes to the chiral records and forms `nabla U_r - i U_(r+1)`. A separate route applies the normalized Spencer inverse, the curvature source and the differentiated lower-record correction. Both routes are compared for every component at `1<=r<=3` and both output chiralities; the completely upper projection is checked separately. The 520 comparisons are finite exact equalities on this metric.

## Environment and entry point

The recorded image is `sagemath/sagemath:10.9`, digest `sha256:e068670ae5863b54b2550e72437ec637b0283acb0dc712c8584c124dbf44e667` (the local image ID). The mathematical entry point is:

```sh
sage -python check_kasner_recursion.py --max-r 3
```

It must run inside the limited container, since it verifies actual cgroup CPU, memory, swap and PID limits before importing Sage. On the recorded host the complete entry point is:

```sh
python3 run_isolated_check.py --max-r 1
python3 run_isolated_check.py --max-r 3
```

The controller is host-specific: it acquires `/Users/studio/.local/state/math-job.lock`, checks the existing Docker services and starts one foreground container. The memory-plus-swap bound is 1,992,294,400 bytes with zero swap, CPU one core, 64 PIDs, a read-only root, network disabled, restart disabled and bounded logs/output. The internal timeout is 880 seconds with forced termination after five more seconds; an independent controller kill applies at 895 seconds. The container is confirmed stopped before the controller removes its own lock. The result JSON records the actual Docker and runtime cgroup limits.

Both supplied runs passed. The order-three program took 2.304 seconds and used 335,732 KiB maximum RSS. These timings and the resource readings describe the supplied runs; the proof in §§5–7 establishes the general theorem.
