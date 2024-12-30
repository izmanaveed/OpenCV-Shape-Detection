# OpenCV-Shape-Detection

## Detecting objects
The first step is to detect the objects under observation and locate their boundaries. The laptop webcam is used for streaming the video and detecting objects in real time. 
The objects are detected using the HSV color space. Trackbars are created to change and track the color values in real time. 

## Finding contours
Next, we need to find contours of the objects and use the blur property on the frame to remove background noise and get clean contours. The HSV trackbar levels will determine which color you are able to detect. 

## Detecting shapes
To identify the shape, we simply count the number of contour sides. Then we define a name for each category. To remove small noise and dots from the background, we choose the contours for greater than 400 pixels. Finally, we count the sides of the contours and give a name accordingly. 
•	For 3 sides, we have a triangle. 
•	For 4 sides, we have a rectangle. 
•	For 5-10 sides, we have a circle.

![image](https://github.com/user-attachments/assets/1fe71fad-7085-439c-813d-364f03e67630)
![image](https://github.com/user-attachments/assets/30e7875d-741f-4596-9063-89470b30c2c5)
![image](https://github.com/user-attachments/assets/443f2d48-b825-44a3-8160-ac4bdb99cba6)
![image](https://github.com/user-attachments/assets/8a70f557-b921-4ad8-ab23-b4e35cb0a0d8)


