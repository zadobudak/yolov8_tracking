# Import essential libraries
import requests
import cv2
import numpy as np
import imutils

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "https://192.168.6.176:8080/shot.jpg"
img = cv2.VideoCapture(4, cv2.CAP_DSHOW)


# While loop to continuously fetching data from the Url
while True:
    try:
        ret,im = img.read()
        print(im.shape)

        # img = imutils.resize(img, width=1080, height=1800)
        cv2.imshow("Android_cam", im)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            break
    except:
        print('error')
        pass

cv2.destroyAllWindows()
