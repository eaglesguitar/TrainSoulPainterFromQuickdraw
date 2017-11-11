#!/usr/bin/env zsh
set -e
mkdir -p log
LOG=log/log-$(date +%Y-%m-%d-%H-%M-%S).log
$CAFFE_ROOT/build/tools/caffe train --solver=/Users/Gerald/development/codes/ai/work/sng_ai_match/make_lmdb_from_quickdraw/lenet_solver.prototxt 2>&1 | tee $LOG $@
