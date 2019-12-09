# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:59:03 2019

@author: 1605458
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:31:00 2019

@author: 1605458
"""
import base64
import json
import urllib.parse
from PIL import Image
import PIL.Image
import tempfile
import numpy as np
#import imutils
from flask import Flask, request
from flask_cors import CORS
import pytesseract
import cv2
import re
import io
app = Flask(__name__)
CORS(app)
@app.route('/predict', methods=['POST'])
def getdate():
    if request.method == 'POST':
        
        '''data= request.data
        image_encode=data["base_64_image_content"]
        print(image_encode)'''
        data=request.get_json()
        image_encode_string=data["base_64_image_content"]
        #image_encode = urllib.parse.unquote(image_encode_string)
        imagestr_as_bytes1 = str.encode(image_encode_string)
        #imagestr_as_bytes = base64.b64encode(imagestr_as_bytes1)
        #print(type(imagestr_as_bytes))
        decoded_string = base64.b64decode(imagestr_as_bytes1)
        #decoded_img = np.fromstring(decoded_string, dtype=np.uint8)
        #print(decoded_img)
        #image_decode=base64.decodestring(imagestr_as_bytes)

        #image_decode=base64.decodebytes(image_encode)
        # print(imagestr_as_bytes)
        img = Image.open(io.BytesIO(decoded_string))
        # # print(img)
        #cv2_img = cv2.cvtColor(decoded_img, cv2.COLOR_RGB2BGR)
        #cv2.imwrite("reconstructed.jpg", cv2_img)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        TESSDATA_PREFIX = 'C:/Users/KIIT/tessdata-master'
        output = pytesseract.image_to_string(img, lang='eng')
        # #s=output.replace(" ", "")
        #print (output)
        pattern1='((\d{1,2})[-|/|\.]((\d{1,2})|([A-Z]*([a-z]+|[a-z]*)))[-|/|\.](\d{2,4}))'
        pattern2='(([A-Z]*([a-z]+|[a-z]*))(\d{1,2}| |\.)(\'|\d{1,2})(\'|\,)\d{2,4})'
        pattern3='(\d{1,2}([A-Z]*([a-z]+|[a-z]*))[\'|\,]\d{2,4})'      
    
        match = re.findall(pattern1, output)
        if len(match)==0:
            match = re.findall(pattern2, output)
        if len(match)==0:
            match = re.findall(pattern3, output)
        print("SUCCESS")    
        #print(match[0][0])
        if len(match)==0:
            return "couldn't recognise"
        else:    
            s=str(match[0][0])
            if len(s)==0:
                return "couldn't identify"
            else:    
                print(s)
                return s
        print("ok")

if __name__ == '__main__':
    app.run(threaded=True)        


