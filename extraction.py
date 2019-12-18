import cv2
import pytesseract
import numpy as np
import pandas as pd
from pytesseract import Output
import re

#seting path of tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
#reading tesseract
img=cv2.imread(r'C:\Users\KIIT\OCR DATA\img1.jpg')
#extraction information from image like top,left,width,heigth,confidence,text
output_dict=pytesseract.image_to_data(img,output_type=Output.DICT)
print(output_dict)
#regex for dates
date_pattern='^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-(19|20)\d\d$'
order_id_pattern='(OD\d+)'
total_amount_pattern='(\d+[.]\d\d)'
#building boxes around the text having >60% of confidence.
#follows the pattern
l=[]
d=[]
boxes=len(output_dict['text'])
for i in range(boxes):
    if int(output_dict['conf'][i])>60:
        if re.match(date_pattern,output_dict['text'][i]) or re.match(order_id_pattern,output_dict['text'][i]):
            x,y,w,h = output_dict['left'][i],output_dict['top'][i],output_dict['width'][i],output_dict['height'][i]
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            l.append(output_dict['text'][i])
        if re.match(total_amount_pattern,output_dict['text'][i]):
            x,y,w,h = output_dict['left'][i],output_dict['top'][i],output_dict['width'][i],output_dict['height'][i]
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            d.append(output_dict['text'][i])
        #else:
           # print('not')
cv2.imshow('img',img)
cv2.waitKey(0)
print("Order ID: "+l[0])
print("Order Date: "+l[1])
print("Invoice Date: "+l[2])
print("Total Amount: "+d[-1])
print(l)
print(d)