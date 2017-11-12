#!/usr/bin/env zsh
set -e
mkdir -p log
LOG=log/log-$(date +%Y-%m-%d-%H-%M-%S).log
$CAFFE_ROOT/build/tools/caffe train --solver=lenet_solver.prototxt 2>&1 | tee $LOG $@
