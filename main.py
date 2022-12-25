import cv2 #manggil library opencv2
import numpy as np #manggil library numpy
#import serial   #manggil library serial

def nothing(x):
    pass

#ser = serial.Serial('COM21') #mendefenisikan fungsi serial
cap = cv2.VideoCapture(1) #mengambil videocapture

ret = cap.set(3,640) #atur resolusi panjang
ret = cap.set(4,480) #atur resolusi lebar
kernel = np.ones((5,5),np.uint8)

#Loop / Perulangan tak hingga
while True:
    area1 = 0
    area2 = 0
    area3 = 0
    #input nilai fokus dari trakbar
    value = cv2.getTrackbarPos("value","Fokus")
    #pengambilan data dari kamera
    ret, img = cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #memasukan nilai ke array Hijau
    hijau_lower = np.array([36,25,25])
    hijau_upper = np.array([70,255,255])
    
    #memasukan nilai ke array Orange
    orange_lower = np.array([4,100,100])
    orange_upper = np.array([18,255,255])

    #memasukan nilai ke array Merah
    merah_lower = np.array([170,70,50])
    merah_upper = np.array([180,255,255])

    #masking warna dari hsv menjadi hiram putih pada setiap layar
    hijau = cv2.inRange(hsv, hijau_lower, hijau_upper)
    orange = cv2.inRange(hsv, orange_lower, orange_upper)
    merah = cv2.inRange(hsv, merah_lower, merah_upper)
    
    #morphological opening (membuka filter untuk perbaikan gambar)
    hijau = cv2.erode(hijau,kernel,iterations=2)
    hijau = cv2.dilate(hijau,kernel,iterations=2)

    orange  = cv2.erode(orange,kernel,iterations=2)
    orange = cv2.dilate(orange,kernel,iterations=2)

    merah = cv2.erode(merah,kernel,iterations=2)
    merah = cv2.dilate(merah,kernel,iterations=2)

    #morphological closing (menutup filter untuk perbaikan gambar)
    hijau = cv2.dilate(hijau,kernel,iterations=2)
    hijau = cv2.erode(hijau,kernel,iterations=1)

    orange = cv2.dilate(orange,kernel,iterations=2)
    orange = cv2.erode(orange,kernel,iterations=1)

    merah = cv2.dilate(merah,kernel,iterations=2)
    merah = cv2.erode(merah,kernel,iterations=1)
    
    #membaca data kamera hasil masking pada warna hijau = tomat mentah 
    (contours,hierarchy)=cv2.findContours(hijau,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        area1 = area

    #membaca data kamera hasil masking pada warna orange = Tomat setengah matang
    (contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        area2 = area
    
    #membaca data kamera hasil masking pada warna merah = Tomat matang
    (contours,hierarchy)=cv2.findContours(merah,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        area3 = area

    if area1>800: print("Tomat Mentah")
    elif area2>800: print("Tomat Setengah Matang")
    elif area3>800: print("Tomat Matang") 
    
               
               
    cv2.imshow("Frame",img)      #menampilkan frame utama gambar dari kamera
    cv2.imshow("hijau",hijau)   #Menampilkan frame hasil masking warna hijau
    cv2.imshow("orange",orange) #Menampilkan frame hasil masking warna orange
    cv2.imshow("merah",merah)   #Menampilkan frame hasil masking warna merah

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() #Menutup Kamera
cv2.destroyAllWindows() #Mematikan program

