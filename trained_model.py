cap.release()

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# Get the training data we previously made
data_path = './faces/user1/'  #give file path where you want to load the data samples
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
# Create arrays for training data and label
Training_Data, Labels = [], []
    # Open training images in our datapath
    # Create a numpy array for training data
    
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

    # Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

    # Initialize facial recognizer
    # model = cv2.face.createLBPHFaceRecognizer()
    # NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()
    # pip install opencv-contrib-python
    # model = cv2.createLBPHFaceRecognizer()
model  = cv2.face_LBPHFaceRecognizer.create()
    # Let's train our model
    
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")
    
