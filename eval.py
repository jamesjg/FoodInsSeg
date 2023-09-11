#%matplotlib inline
import json
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab
from pycocotools import mask as maskUtils

annType = ['segm']    #specify type here
prefix = 'instances'
print('Running demo for *%s* results.'%(annType))



#initialize COCO ground truth api
annFile = r'FoodInsSeg\annotations\Test.json'
cocoGt=COCO(annFile)



#initialize COCO detections api
resFile=r'results\results.json'
cocoDt=cocoGt.loadRes(resFile)


imgIds=sorted(cocoGt.getImgIds())

cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
