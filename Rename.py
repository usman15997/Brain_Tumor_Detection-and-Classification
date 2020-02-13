# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 02:10:03 2020

@author: usman
"""

import cv2


import os
g=0
m=0
p=0

# Renaming the Original Image files 
path = r'C:\Users\usman\darkflow-master\DIPA_DataSet\Original_Testing'

if __name__=='__main__':
    for n, image_file in enumerate(os.scandir(path)):
        img=image_file
        splited_name=img.name.split('.')
        print(splited_name[0])
        if '1' in splited_name:
            m=m+1
            image=cv2.imread(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Original_Testing/'+str(img.name))
            cv2.imwrite(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing\ '+str(m)+'M.jpg',image)
        if '2' in splited_name:
            g=g+1
            image=cv2.imread(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Original_Testing/'+str(img.name))
            cv2.imwrite(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing\ '+str(g)+'G.jpg',image)
        if '3' in splited_name:
            p=p+1
            image=cv2.imread(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Original_Testing/'+str(img.name))
            cv2.imwrite(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing\ '+str(p)+'P.jpg',image)
        img=None
        image=None
        splited_name=None
        #img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        #cv2.imwrite(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Renamed_testing' + str(j) + '.jpg', img)
