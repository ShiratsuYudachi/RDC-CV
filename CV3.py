# import the necessary packages
import cv2
import numpy as np

# color ranges in bgr order for inRange function
## you will need to tune the values based on your camera and real-world condition ##
## since in different environment, the color of the box may be different because of the light or some other factors ##

lower_red = np.array([0, 43, 46]) 
higher_red = np.array([10, 255, 255])
lower_green = np.array([35, 43, 46])
higher_green = np.array([77, 255, 255])
lower_blue = np.array([78, 43, 46])
higher_blue = np.array([124, 255, 255])
font = cv2.FONT_HERSHEY_SIMPLEX

# capture the video from the camera
## 0 means the first camera, If your computer has a built-in webcam, then "0" typically represents it ##
## so if you have an external camera, you may need to change it to "1" or "2" ##
cap = cv2.VideoCapture(0)

# check if the camera is opened successfully
while cap.isOpened():
    # capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        if frame is not None:
            ###### main part of your code ######
            ## example ##
            
            img_hav = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#change RGB to HSV
            mask_red = cv2.inRange(img_hav, lower_red, higher_red)
            mask_green = cv2.inRange(img_hav, lower_green, higher_green)
            mask_blue = cv2.inRange(img_hav, lower_blue, higher_blue)
            mask_red = cv2.medianBlur(mask_red ,7)
            mask_green = cv2.medianBlur(mask_green ,7)
            mask_blue = cv2.medianBlur(mask_blue ,7)
            cnt_red, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt_green, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt_blue, hierarchy = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in cnt_red:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, "red",(x, y - 20), font, 0.7, (0, 0, 255), 2)
                #print("getting image")

            for cnt in cnt_blue:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, "blue",(x, y - 30), font, 0.7, (255, 0, 0), 2) #change it to blue later on
                #print("getting image")

            for cnt in cnt_green:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y - 50), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "green",(x, y - 50), font, 0.7, (0, 255, 0), 2)
                #print("getting image")

            # show the frame
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
            
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
            ###### end of this main part ######

# when everything is done, release the capture and close all windows

