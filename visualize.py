import os
import numpy as np
from pycocotools.coco import COCO
from skimage import io
from matplotlib import pyplot as plt
import json
import cv2

if __name__=='__main__':

    json_file = r'FoodInsSeg\annotations\Test.json'
    imgsPath = r'FoodInsSeg\images\test'

    jsonFile = json.load(open(json_file))
    classId2className = jsonFile['categories']
    imId2imageNames = {}

    for imgs in jsonFile['images']:
        imId2imageNames[imgs['id']] = imgs['file_name']
    imgId2labels = {}

    for label in jsonFile['annotations']:
        imgId = label['image_id']
        if imgId not in imgId2labels:
            imgId2labels[imgId] = []
        imgId2labels[imgId].append(label)

    coco = COCO(json_file)

    for imgId in sorted(imgId2labels.items(), key=lambda x:int(x[0])):
        imgName = imId2imageNames[imgId[0]]
        img = io.imread(os.path.join(imgsPath,imgName))
        plt.figure(imgName)
        plt.axis('off')
        plt.imshow(img) 
        coco.showAnns(imgId2labels[imgId[0]])
        print(imgName)
        plt.show()  
    
