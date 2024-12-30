import cv2
import numpy as np

def nothing(x):
    # any operation
    pass
cap = cv2.VideoCapture(0) #start videostreaming through webcam

#creating trackbars to control HSV levels for shape detection
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #detecting color using HSV

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    #getting the live values from trackbar
    lower_range =  np.array([l_h, l_s, l_v]) 
    upper_range = np.array([u_h, u_s, u_v])  
    mask = cv2.inRange(hsv, lower_range, upper_range)
  
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel) 


##  Finding contours

    # Contours detection
    if int(cv2.__version__[0]) > 3:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

## Detecting shapes

    for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 400:
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 3:
                    cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0)) #detect triangle
                elif len(approx) == 4 :
                    cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0)) #detect rectangle
                elif 5 < len(approx) < 10:
                    cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0)) #detect circle


        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()