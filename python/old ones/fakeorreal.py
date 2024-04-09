import numpy as np
import argparse
import cv2
import os
ap = argparse.ArgumentParser()
ap.add_argument("-i","--input",type=str,required=True,help="path to input video")
ap.add_argument("-o","--output",type=str,required=True,help="path to output directory of the cropped faces")
ap.add_argument("-d","--detector",type=str,required=True,help="path to OpenCV's deep learning face detector")
ap.add_argument("-c","confidence",type=float,default=0.5,help="minimum probability to filter weak detection")
ap.add_argument("-s","--skip",type=int,default=16,help="# of frames to skip  before applying face detection")
args=vars(ap.parse_args())
print("[INFO] loading face detector...")
protoPath= os.path.sep.join([args["detector"],deploy.prototxt"])
modelPath
