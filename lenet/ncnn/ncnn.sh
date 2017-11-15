#!/usr/bin/env sh
caffe2ncnn deploy.prototxt quick_draw_lenet_iter_10000.caffemodel lenet.param lenet.bin
ncnn2mem lenet.param lenet.bin lenet.id.h lenet.mem.h