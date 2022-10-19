### Setup

Install TensorFlow on Raspberry Pi through pip. 

```bash
sudo apt update
sudo apt install python3-dev python3-pip
sudo apt install libatlas-base-dev        # required for numpy
```

```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade tensorflow

# Test TensorFlow
```bash
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000,1000])))"
```
# Install OpenCV2
 ```bash
sudo apt install libtiff5-dev libjasper-dev libpng12-dev
pip install pillow jupyter matplotlib cython
pip install opencv-python
```

Download MobileNet-SSD v2 [weights](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz) and [config](https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/ssd_mobilenet_v2_coco_2018_03_29.pbtxt).

### Programs

1.py - camera output directly into frame buffer. 

2.py - capture image from camera, performan
object detection, draw recognized objects with labels into image and
display image in an X window.  
