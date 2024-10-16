import cv2
import numpy as np

page = np.ones((512, 512, 3), dtype=np.uint8) * 255 # Beyaz background


#Geometrik şekilleri çiz
cv2.rectangle(page, (50, 50), (150, 150), (0, 255, 200), thickness=-1) #Kare
cv2.circle(page, (400, 400), 70, (0, 0, 255), thickness=-1) # Daire

points = np.array([[256, 150], [156, 400], [300, 400]]) #Üçgen
cv2.fillPoly(page, [points], (0, 0, 0))
#cv2.imshow("Unedited", page) # Editsiz halini göster

gray = cv2.cvtColor(page, cv2.COLOR_BGR2GRAY) #griye çevir, renklerle uğraşma (sınır hatları)
Canny = cv2.Canny(gray, 150,150) # canny şekil tespitine yarar

contours, _ = cv2.findContours(Canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area = cv2.contourArea(cnt) #kontur alanları
    if area > 1000: #alanlar 1000den büyük olanı alma (gürültü)
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cornerCount = len(approx) #şekil uzunluğuna göre köşe
        x,y, w, h = cv2.boundingRect(approx) #şeklin etrafına görünmez diködrtgen, bunun üzerinden yazı yazma işlemi
        if (cornerCount == 3):
            cv2.putText(page, "Ucgen", (x+5, y+5), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
        elif (cornerCount == 4):
            cv2.putText(page, "Kare", (x + 5, y + 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        else:
            cv2.putText(page, "Daire", (x + 5, y + 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        cv2.drawContours(page, cnt, -1, (0, 255, 0), 3)

#çıktı
#cv2.imshow("Test", Canny)
cv2.imshow('Task', page)
tus = cv2.waitKey(0)
if tus == 27:
    cv2.destroyAllWindows()
elif tus == ord("d"):
    cv2.imwrite("BasitSekiller.jpg", page) # klavyede escye basılınca fotoğraf kapanır, d harfine basıldığında fotoğraf YeniGoruntu.jpg şeklinde kaydedilir.
















