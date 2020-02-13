# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:07:40 2020

@author: usman
"""

import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
#%config InlineBackend.figure_format='svg'
import os 
from sklearn.metrics import classification_report,confusion_matrix
#from imblearn.metrics import sensitivity_specificity_support

#from sklearn.utils.validation import check_array

options ={
    'model' : 'cfg/tiny-yolo-voc-3c.cfg',
    'load' : 1000,
    'threshold': 0.02,
    'gpu' : 1.0
}

tfnet= TFNet(options)

#Label='Gliomia_tumour'
Label=[]
Prediction=[]



image_folder = r"C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing"

#'Pituirity_tumour' or 'Gliomia_tumour' Menigiomia
if __name__=='__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img=cv2.imread(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing/'+str(image_file.name))
        result=tfnet.return_predict(img)
        Prediction.append(result[0]['label'])
        if 'G' in image_file.name:
            Label.append('Gliomia_tumour')
        if 'M' in image_file.name:
            Label.append('Menigiomia_tumour')
        if 'P' in image_file.name:
            Label.append('Pituirity_tumour')
        
        
        
        
print(classification_report(Label,Prediction))      
print(confusion_matrix(Label,Prediction))
