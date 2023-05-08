import face_recognition as fr
import cv2
import openpyxl as oxl
import pickle
import numpy as np
import pyautogui as pag
import time
import serial

vid = cv2.VideoCapture(0)

workbook = oxl.load_workbook('Data.xlsx')
xcl = workbook.get_sheet_by_name('Lapa1')
Img_number = xcl["E2"].value

numofrec = [0]*50

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

n = 1

while( n == 1):
  try:    
    ret, new = vid.read()
    cv2.imshow('new', new)
    cv2.waitKey(1)
    i = 1

    while(i <= Img_number):

        data_name = xcl['C'+str(i+4)].value

        rgb_img = cv2.cvtColor(new, cv2.COLOR_BGR2RGB)
        img_encoding = fr.face_encodings(rgb_img)

        with open(str(data_name),'rb') as f:
            face_to_compare = pickle.load(f)

        result = fr.compare_faces(img_encoding,face_to_compare)
    

        for x in result:
           
            if(x == [True]):
                print(xcl["F"+str(i+4)].value)
                write_read(xcl["F"+str(i+4)].value)
                time.sleep(2)
                print("Faces match?: ", x)
                numofrec[i] = numofrec[i] + 1
                xcl["I"+(str(i+4))].value = numofrec[i]
                break

        i = i + 1

  except KeyboardInterrupt:
    pass
    n = 0

workbook.save("Data.xlsx")