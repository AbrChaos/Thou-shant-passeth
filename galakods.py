import cv2
import face_recognition as fr
import numpy as np
import openpyxl as oxl
import pickle
import pyautogui as pag
import PySimpleGUI as sg
import time
import serial

workbook = oxl.load_workbook('Data.xlsx')
xcl = workbook.get_sheet_by_name('Lapa1')
Img_number = xcl["E2"].value

vid = cv2.VideoCapture(0)



screenshot_done = False
    
layout = [[sg.Text("Iestatīt jaunu seju, vai palaist sejas atpazīšanu")], [sg.Button("Iestatīt jaunu seju")],[sg.Button("palaist sejas atpazīšanu")], ]

window = sg.Window("Izvēlne", layout)

while True:
    event, values = window.read()

    if  event == sg.WIN_CLOSED:
        break
    if event == "Iestatīt jaunu seju":

        name = pag.prompt(text='Enter your name(use _ instead of space):', title='Name' , default='Name')

        while (screenshot_done == False) :
            ret, frame = vid.read()

            cv2.imshow('nospiest q lai uzņemtu bildi', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                result, screenshot = vid.read()
                screenshot_done = True
                cv2.destroyWindow("nospiest q lai uzņemtu bildi")

            confirmed = False

        while(confirmed == False):
            cv2.imshow('screenshot', screenshot)
            choice = pag.confirm(text='Use this image, or retry', title='Confirm', buttons=['Confirm', 'Retry'])
                
            if(choice == 'Confirm'):
                    
                   
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


    if event == "palaist sejas atpazīšanu":
        
        window.close()

        layout = [[sg.Text(size=(20,1), key='-TEXT3-')],[sg.Text(size=(20,1), key='-TEXT-')], [sg.Text(size=(20,1), key='-TEXT2-')], [sg.Text('vērtības')]]

        window2 = sg.Window("Atpazīšana", layout, size=(200,100))

        arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
        
        while True:
                event, values = window2.read(timeout=1000)

                if  event == sg.TIMEOUT_KEY:

                    vid = cv2.VideoCapture(0)

                    workbook = oxl.load_workbook('Data.xlsx')
                    xcl = workbook.get_sheet_by_name('Lapa1')
                    Img_number = xcl["E2"].value

                    numofrec = [0]*50

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
                                        window2['-TEXT3-'].update("atrasta seja")
                                        window2['-TEXT2-'].update(xcl["F"+str(i+4)].value)
                                        write_read(xcl["F"+str(i+4)].value)
                                        time.sleep(2)
                                        print("sejas sakrīt?: ", x)
                                        window2['-TEXT-'].update(("sejas atpazīta?: "+ str(x)))
                                        numofrec[i] = numofrec[i] + 1
                                        xcl["I"+(str(i+4))].value = numofrec[i]
                                        n = 0
                                        break
                                        

                                i = i + 1

                        except event == sg.WIN_CLOSED:
                            pass
                            window2.close()
                elif event == sg.WIN_CLOSED:
                    break

        

workbook.save("Data.xlsx")
window2.close()