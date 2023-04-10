import face_recognition as fr
import cv2
import openpyxl as oxl
import pickle
import numpy as np
import pyautogui as pag
import time


vid = cv2.VideoCapture(0)

workbook = oxl.load_workbook('Data.xlsx')
xcl = workbook.get_sheet_by_name('Lapa1')
Img_number = xcl["E2"].value

i = 1

while(True):
    
    ret, new = vid.read()
    cv2.imshow('new', new)
    cv2.waitKey(1)

    while(i <= Img_number):

        data_name = xcl['C'+str(i+4)].value

        rgb_img = cv2.cvtColor(new, cv2.COLOR_BGR2RGB)
        img_encoding = fr.face_encodings(rgb_img)

        with open(str(data_name),'rb') as f:
            face_to_compare = pickle.load(f)

        result = fr.compare_faces(img_encoding,face_to_compare)
    
        print("Faces match?: ", result )

        if(result == [True]):
            print(xcl["F"+str(i+4)].value)
            pag.alert(text=xcl["F"+str(i+4)].value, title='', button='OK')
            time.sleep(7)
        
        i = i+1

    if(result == True): break
    i = 1

print("Faces match?: ", result )

