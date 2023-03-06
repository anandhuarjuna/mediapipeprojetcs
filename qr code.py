import cv2
import pyzbar.pyzbar as pyzbar
from selenium import webdriver

driver=webdriver.Chrome()

cap=cv2.VideoCapture(0)
while True:
    sucess,image=cap.read()
    if not sucess:
        break

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    qrcodes=pyzbar.decode(gray)

    for qrcode in qrcodes:
        data=qrcode.data.decode('utf-8')

        driver.get(data)

    cv2.imshow('img',image)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
driver.quit()