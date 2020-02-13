# Brain_Tumor_Detection-and-Classification
Brain_Tumor_Detection and Classification using YOLO v2 

1) First I use contours to make annotations file(.xml files) of training set (\darkflow-master\DIPA_DataSet\DataSet\) and for that i used contour testing.py file 
(what is does is it basically takes the original tumour image and use its name to search for its respective label and find its contour and then use the coordinates of contours to make annotation file) 
2) I collected the annotation files in Annotations folder (\darkflow-master\DIPA_DataSet\Annotations\)
3) For training open ANACONDA command prompt in current directory and type this following command:
python flow --model darkflow-master\cfg\tiny-yolo-voc-3c --load darkflow-master\bin\tiny-yolo-voc.weights --dataset darkflow-master\DIPA_DataSet\training --annotations \darkflow-master\DIPA_DataSet\Annotations\ --epoch 10

here model means which model (for how many classes you want to train) so i made it to work for 3 classes by making changes in darkflow-master\cfg\tiny-yolo-voc i.e final layer neurons become 3 and # of filters become 5*(5+3)=40 and 3 here represent 3 classes
i downloaded the initial weights from (https://pjreddie.com/darknet/yolo/) so --load basically loads the initial weights 
then i provided the dataset and annotations and no. of epochs 

i am saving weights in ckpt folder after every 125 steps.

After training i tested my model on test set which contains 606 images 
(darkflow-master\DIPA_DataSet\Original_Testing)

then with the help of Scikit-learn i made confuion matrix and calculated performance parameters i.e fscore, precision, recall and accuracy.


Note:

I used rename.py just to rename files as yolo doesn't recognize filenames with hyphen in it. 

P.S I followed these (https://www.youtube.com/watch?v=PyjBd7IDYZs&list=PLX-LrBk6h3wSGvuTnxB2Kj358XfctL4BM) tutorials on youtube.

the instructor in this video worked on just one class but he guided me how to make yolo work for multiclass and what need to modify etc. and he worked with video (which yolo is designed for i.e real time detection)) 
but i don't have good pc with GPU and good Ram so i used Images and worked with that.


If you need more details follow his tutorial it's super cool.

Thanks 

   
