#!/usr/bin/env bash
set -euo pipefail
release_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
paper_dir="$release_root/paper"
output_dir="$release_root/build/paper"
mkdir -p "$output_dir"
cd "$paper_dir"
for pass_number in 1 2 3; do
  TEXINPUTS=".:$paper_dir:" pdflatex -recorder -interaction=nonstopmode         -halt-on-error -output-directory="$output_dir" "$paper_dir/manuscript.tex"         > "$output_dir/pass${pass_number}.log" 2>&1
done
printf '%s\n' "$output_dir/manuscript.pdf"
