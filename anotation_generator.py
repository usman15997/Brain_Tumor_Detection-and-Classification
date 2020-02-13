# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 24 03:04:14 2019
# 
# @author: usman
# """
# 
# import os 
# import matplotlib.pyplot as plt
# import cv2
# from matplotlib.widgets import RectangleSelector
# 
# from Automated_annotator import write_xml
# 
# #global_constant
# 
# img=[]
# 
# tl_list=[]
# 
# br_list=[]
# 
# object_list=[]
# 
# #constants 
# 
# image_folder = r"C:\Users\usman\darkflow-master\DIPA_DataSet\M"
# 
# savedir= r"C:\Users\usman\darkflow-master\DIPA_DataSet\annotations_testing"
# 
# obj="Menigiomia_tumour"
# 
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
# 
# if __name__=='__main__':
#     for n, image_file in enumerate(os.scandir(image_folder)):
#         img=image_file
#         
#         fig, ax =plt.subplots(1)
#         
#         image=cv2.imread(image_file.path)
#         
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
# 
# 
# =============================================================================

# this file is to make rectangle one by one on each image and then use its coordinate to make annotations
import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector

from Automated_annotator import write_xml

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = r"C:\Users\usman\darkflow-master\DIPA_DataSet\M"
# 
savedir= r"C:\Users\usman\darkflow-master\DIPA_DataSet\annotations_testing"
obj = 'M'


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        print(object_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
# =============================================================================
#         mngr =plt.get_current_fig_manager()
#         mngr.window.setGeometry(250, 120, 1280, 1024)
# =============================================================================
        
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()