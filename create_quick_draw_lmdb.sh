#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

DATA_ROOT=data
CAFFE_TOOLS=$CAFFE_ROOT/build/tools

TRAIN_IMAGE_ROOT=$DATA_ROOT/quickdraw_train_image/
TRAIN_MAPPING_FILE=$DATA_ROOT/quickdraw_train.txt
TRAIN_OUTPUT_LMDB=$DATA_ROOT/quickdraw_train_lmdb

TEST_IMAGE_ROOT=$DATA_ROOT/quickdraw_test_image/
TEST_MAPPING_FILE=$DATA_ROOT/quickdraw_test.txt
TEST_OUTPUT_LMDB=$DATA_ROOT/quickdraw_test_lmdb

VAL_IMAGE_ROOT=$DATA_ROOT/quickdraw_val_image/
VAL_MAPPING_FILE=$DATA_ROOT/quickdraw_val.txt
VAL_OUTPUT_LMDB=$DATA_ROOT/quickdraw_val_lmdb

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=28
  RESIZE_WIDTH=28
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_IMAGE_ROOT" ]; then
  echo "Error: TRAIN_IMAGE_ROOT is not a path to a directory: $TRAIN_IMAGE_ROOT"
  echo "Set the TRAIN_IMAGE_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_IMAGE_ROOT" ]; then
  echo "Error: VAL_IMAGE_ROOT is not a path to a directory: $VAL_IMAGE_ROOT"
  echo "Set the VAL_IMAGE_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

if [ -d "$TRAIN_OUTPUT_LMDB" ]; then
  if [ "$(ls -A $TRAIN_OUTPUT_LMDB)" ]; then
       echo "$TRAIN_OUTPUT_LMDB is not Empty, clear it first"
       exit 1
  fi
fi

if [ -d "$TEST_OUTPUT_LMDB" ]; then
  if [ "$(ls -A $TEST_OUTPUT_LMDB)" ]; then
       echo "$TEST_OUTPUT_LMDB is not Empty, clear it first"
       exit 1
  fi
fi

if [ -d "$VAL_OUTPUT_LMDB" ]; then
  if [ "$(ls -A $VAL_OUTPUT_LMDB)" ]; then
       echo "$VAL_OUTPUT_LMDB is not Empty, clear it first"
       exit 1
  fi
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $CAFFE_TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --gray \
    $TRAIN_IMAGE_ROOT \
    $TRAIN_MAPPING_FILE \
    $TRAIN_OUTPUT_LMDB

echo "Creating test lmdb..."

GLOG_logtostderr=1 $CAFFE_TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --gray \
    $TEST_IMAGE_ROOT \
    $TEST_MAPPING_FILE \
    $TEST_OUTPUT_LMDB

echo "Creating val lmdb..."

GLOG_logtostderr=1 $CAFFE_TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --gray \
    $VAL_IMAGE_ROOT \
    $VAL_MAPPING_FILE \
    $VAL_OUTPUT_LMDB

echo "Done."
