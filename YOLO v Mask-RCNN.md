# YOLOv3 and Mask R-CNN Comparison

This document will serve as a sort of sketchpad to mark the two major approaches considered in this object localization project.
What's more, it will ultimately serve as justification for choosing the approach that we did.

## YOLOv3

* A refinement of YOLOv2 which was a refinement of the basic architecture of YOLOv1
* Built just for object detection
* Since YOLO is a single stage architecture, it's ultimately simpler to implement
* Faster inference times also mean faster training times

## Mask R-CNN

* Built for both object detection and segmentation
* Generally regarded as the superior approach do to it's incredibly fast and accurate predictions
* Multi-stage architecture means a more complex implementation
* Longer training times

## Decision

Although technically a lower performer that Mask R-CNN, we will be opting for the simpler YOLOv3 approach.
More specifically, we'll be deploying the popular third-party implementation originally developed by 
[experiencor](https://github.com/experiencor/keras-yolo3)
taking advantage of its open source MIT Licensing. Further, we will be using this 
[tutorial](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/)
as a jumping off point for our project.