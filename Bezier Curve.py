import numpy as np
import cv2

img = np.zeros((500, 500, 3), np.uint8)
img.fill(0)

#Points
ps = []

#Pascal Triangle
pa = [
    [1, 1],         
    [1, 2, 1],      
    [1, 3, 3, 1],   
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1] 
]

#Bezier Curve
def bezier():
    order = len(ps) - 1

    t = 0.001
    while t <= 1:
        B = np.array([0.0, 0.0])
        for i in range(order+1):
            B += pa[order-1][i] * t**i * (1-t)**(order-i) * ps[i]

        img[int(B[1])][int(B[0])] = 255

        cv2.imshow('1', img)
        if cv2.waitKey(1) == 113:
            return 0

        t += 0.001

#Mouse Events
def event(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        ps.append(np.array([x, y]))
        img[y][x] = 255

    if event == cv2.EVENT_RBUTTONDOWN:
        r = ps.pop()
        img[r[1]][r[0]] = 0

    if event == cv2.EVENT_RBUTTONDBLCLK:
        ps.clear()
        img.fill(0)

    if event == cv2.EVENT_MBUTTONDOWN:
        bezier()
        ps.clear()

cv2.namedWindow('1')
cv2.setMouseCallback('1', event) 
while 1:
    cv2.imshow('1', img)
    if cv2.waitKey(1) == 113:
        break

