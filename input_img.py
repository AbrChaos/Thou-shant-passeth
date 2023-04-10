import cv2
import face_recognition as fr
import numpy as np
import openpyxl as oxl
import pickle
import pyautogui as pag
    
workbook = oxl.load_workbook('Data.xlsx')
xcl = workbook.get_sheet_by_name('Lapa1')
Img_number = xcl["E2"].value

vid = cv2.VideoCapture(0)

name = pag.prompt(text='Enter your name(use _ instead of space):', title='Name' , default='Name')

screenshot_done = False

while (screenshot_done == False) :
 ret, frame = vid.read()

 cv2.imshow('frame', frame)

 if cv2.waitKey(1) & 0xFF == ord('q'):
       result, screenshot = vid.read()
       screenshot_done = True
       cv2.destroyWindow("frame")

confirmed = False

while(confirmed == False):
   cv2.imshow('screenshot', screenshot)
   choice = pag.confirm(text='Use this image, or retry', title='Confirm', buttons=['Confirm', 'Retry'])
   
   if(choice == 'Confirm'):
      
     # if (fr.face_encodings(cv2.cvtColor(cv2.imread('Img/'+name+'.jpg'), cv2.COLOR_BGR2RGB))[0] != IndexError):
         cv2.imwrite('Img/'+name+'.jpg', screenshot)
         confirmed = True
         break

   if(choice == 'Retry'):
      
      screenshot_done = False
      cv2.destroyAllWindows()
      vid = cv2.VideoCapture(0)

      while (screenshot_done == False) :
         ret, frame = vid.read()

         cv2.imshow('frame', frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
             result, screenshot = vid.read()
             screenshot_done = True
             cv2.destroyWindow("frame")


img = cv2.imread('Img/'+name+'.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = fr.face_encodings(rgb_img)[0]

with open('encoding\dataset_'+name+'.dat','wb') as f:
 pickle.dump(img_encoding, f)

xcl['E2'].value = Img_number+1
xcl['B'+(str(5+Img_number))].value = Img_number+1
xcl['C'+(str(5+Img_number))].value = 'encoding\dataset_'+name+'.dat'
xcl['F'+(str(5+Img_number))].value = name

workbook.save('Data.xlsx')



