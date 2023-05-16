import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("00tennisballs1-superJumbo.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5 ,minDist=200 ,param1=100, param2=50, maxRadius=100, minRadius=70,)
print(f"circles on image:{circles}")
num_balls=len(circles[0])
print("number of ball in the picture=",num_balls)
if circles is not None:
    circles=circles[0].astype(np.uint32)
    for circle in circles:
        cv2.circle(img, (circle[0], circle[1]), circle[2], (0,0,255), 2)
        cv2.putText(img, str(circles.tolist().index([circle[0], circle[1], circle[2]])+1), (circle[0], circle[1]+circle[2]+20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

print("position of the red ball=",circles[6])

resize= cv2.resize(img, None, fx=0.6, fy=0.6)	

cv2.imshow("image", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
