# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Dec 27 19:51:03 2019
# 
# @author: usman
# """
# 
# import cv2
# import matplotlib.pyplot as plt
# 
# import numpy as np
# from PIL import Image
# 
# from Automated_annotator import write_xml
# 
# image_folder = r"C:\Users\usman\darkflow-master\Gliomia_tumour"
# 
# savedir= r"C:\Users\usman\darkflow-master\DIPA_DataSet\annotations_testing"
# 
# obj="Gliomia_tumour"
# 
# tl=[]
# br=[]
# 
# for i in range(20):
#     img = plt.imread('Gliomia_labels/'+str(i+1)+'.bmp')
#     contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     x,y,w,h=cv2.boundingRect(contours[0])
# # =============================================================================
# #     rectangled=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
# #     tumour=cv2.imread('Gliomia_tumour/'+str(i+1)+'.bmp')
# #     rectangled=cv2.rectangle(tumour,(x,y),(x+w,y+h),(255,0,0),5)
# #     cv2.imwrite( 'Extracted_Gliomia/'+ str(i+1)+'.bmp', rectangled)
# # =============================================================================
#     tl.append((x,y))
#     br.append((x+w,y+h))
#     
#     image=plt.imread('Gliomia_tumour/'+str(i+1)+'.bmp')
#     
#     write_xml(image_folder,image,obj,tl,br,savedir)
#     
#     image=None
#     tl=[]
#     br=[]
# =============================================================================
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 03:04:14 2019

@author: usman
"""

import os 
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector

from Automated_annotator import write_xml

#global_constant

img=[]

tl_list=[]

br_list=[]

object_list=[]

#constants 

image_folder = r"C:\Users\usman\darkflow-master\DIPA_DataSet\DataSet\G"
 
savedir= r"C:\Users\usman\darkflow-master\DIPA_DataSet\Annotations"
 
obj="Gliomia_tumour"

# =============================================================================
# def line_select_callback(clk,rls):
#     global tl_list
#     global br_list
#     tl_list.append((int(clk.xdata), int(clk.ydata)))
#     br_list.append((int(rls.xdata), int(rls.ydata)))
#     object_list.append(obj)
# 
# 
# def onkeypress(event):
#      global tl_list
#      global br_list
#      global object_list
#      
#      global img
#      
#      if event.key == 'q' :
#          write_xml(image_folder,img,object_list,tl_list,br_list,savedir)
#          tl_list=[]
#          br_list=[]
#          object_list=[]
#          img=None
#          
#          
# 
# 
# 
# def toggle_selector(event):
#     toggle_selector.RS.set_active(True)
# =============================================================================
i=1
if __name__=='__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img=image_file
        img_label = plt.imread(r'C:\Users\usman\darkflow-master\DIPA_DataSet\Labels\All/'+str(img.name))
        

        image = cv2.cvtColor(img_label, cv2.COLOR_BGR2GRAY) 
        ret,binary=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

        contours,hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x,y,w,h=cv2.boundingRect(contours[0])
      
        tl_list.append((x,y))
        br_list.append((x+w,y+h))
        print(img.name)
        print(x,y,x+w,y+h)
#==================================================
#         fig, ax =plt.subplots(1)
# =============================================================================
        object_list.append(obj)
       # image=cv2.imread(image_file.path)
        #i=i+1
        write_xml(image_folder,img,object_list,tl_list,br_list,savedir)
        tl_list=[]
        br_list=[]
        object_list=[]
        img=None
         
# =============================================================================
#         ax.imshow(image)
#         
#         toggle_selector.RS = RectangleSelector(
#                 ax, line_select_callback,
#                 drawtype='box' , useblit=True,
#                 button=[1], minspanx=5 , minspany=5,
#                 spancoords='pixels' , interactive = True
#                 )
#         
#         
#         bbox = plt.connect('key_press_event' , toggle_selector)
#         key= plt.connect('key_press_event' , onkeypress)
#         plt.show()
#         plt.close()
#         
# =============================================================================


