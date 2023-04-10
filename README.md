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
 
 Pirmā programma:
       1. Lietotājam palūdz ierakstīt vārdu
       2. Parāda webkameru, un giada kad lietotājs uzspiedīs "q"
       3. Kad nospiests "q", programma parāda uzņemto bildi, un piedāvā izvēlēties uzņemto, vai uzņemt jaunu.
       4. Izvēlēto bildi pārveido uz datamodeli, saglabā, un excelī ieraksta datus.
 
 Otrā programma veic sejas atpazīšanu, un atgriež atpazīto vārdu. Tā izeja ir pagaidu variants. Izeja rāda [], kad nav atrasta neviena seja, un [false], vai [True], šobrīd, lai programma atgrieztu vārdu, vajadzīga tikai viena redzama seja kadrā. 
 
 ## 3. Papildinājumi
 
     Šobrīd programmas gala izeja ir logs, kas pasaka atpazītās personas vārdu. Izmantojot kkādu arduino library jāaizsūta vārds uz arduino caur serial com. 
     Man liekas, ka arduino galā varētu ielikt lcd displeju, kas parāda vārdu, un kkādu lampiņu, vai pīkstuli, kas norāda, ka atrasta seja.
     




