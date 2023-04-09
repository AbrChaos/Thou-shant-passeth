# Thingi

## 1. Dependencies

#### Ļoti ieteicams izmantot **Anaconda**

###### Izmantoju python 3.9

1.1. Sejas atpazīšanai tiek izmantota bibliotēka **face_recognition**, kas balstās uz bibliotēku **dlib**, un dlib balstās uz **cmake**.
1.2. Sākumā jāinstalē cmake no https://cmake.org/, itkā var izmantot pip install cmake, bet man šķiet ka negāja
1.3. Dlib instalēšana ir lielākā problēma, nevarēju to izdarīt ar parasto pyhton, bet ar anaconda izdevās, izmantojot *conda install -c conda-forge dlib*
1.4. Un galā jāizmanto pip install face_recognition. 

ps. pie šitā var sanākt mazliet pačakarēties

2. Izmantoju **opencv**, jeb cv2 python programmās, lai uzņemtu webkameras bildi.
3. Pielietota bibliotēka **openpyxl**, lai ievietotu datus excel failā.
4. Izmantots **Pickle** lai saglabātu encoding datus.
5. Pat neaceros kam izmantoju **numpy**, bet viņš tur ir
6. Izmantots **pyautogui** priekš GUI
7. Un **time**, lai ieliktu delay, bez tā var mierīgi iztikt

## 2. Īss izklāsts
 
 Pirmā programma uzņem bildi no webkameras, to encod(o) un ieraksta excel failā vārdu un encoding(a) faila nosaukumu. 
 
 Otrā programma veic sejas atpazīšanu, un atgriež atpazīto vārdu.




