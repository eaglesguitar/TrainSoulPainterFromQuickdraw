# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

caffe_root = os.environ.get('CAFFE_ROOT')

sys.path.insert(0, caffe_root + '/python') #把pycaffe所在路径添加到环境变量
import caffe

#指定网络结构 与 lenet_train_test.prototxt不同
MODEL_FILE = 'lenet.prototxt'
PRETRAINED = 'quick_draw_lenet_iter_10000.caffemodel'
#图片已经处理成 lenet.prototxt的输入要求（尺寸28x28）且已经二值化为黑白色
IMAGE_FILE = '../data/quickdraw_val_image/full_Fnumpy_bitmap_Fcat_6501.jpg'

# print os.path.exists(MODEL_FILE)
# print os.path.exists(PRETRAINED)
# print os.path.exists(IMAGE_FILE)

input_image = caffe.io.load_image(IMAGE_FILE, color=False)
net = caffe.Classifier(MODEL_FILE, PRETRAINED)
prediction = net.predict([input_image], oversample = False)
caffe.set_mode_cpu()
print 'predicted class:', prediction
