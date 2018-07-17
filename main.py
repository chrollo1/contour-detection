import cv2
import numpy as np

# open vid
cap = cv2.VideoCapture('<INSERT YOUR VIDEO HERE>.mp4')

# check if vid opened...
if not cap.isOpened():
    print("Error opening video")

# read until vid is complete
while cap.isOpened:
    ret, frame = cap.read()
    blur_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

    low = np.array([29, 86, 6])
    hi = np.array([64, 185, 255])
    fgmask = cv2.inRange(hsv, low, hi)

    ret, contours, ret = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        # if above threshold
        if area > 2000:
            # draw
            cv2.drawContours(frame, contour, -1, (0, 0, 255), 3)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", fgmask)

    key = cv2.waitKey(1)
    # esc to exit
    if key == 27:
        break

# release capture and close
cap.release()
cv2.destroyAllWindows()
