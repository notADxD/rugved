import cv2 as cv
import numpy as np

# Define the upper and lower bounds for green in HSV color space
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

video = cv.VideoCapture('green.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_green, upper_green)

    contours, _ = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area > 100:
            cv.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    cv.imshow('Original', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
