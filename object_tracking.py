import cv2
import os

tracker = cv2.TrackerCSRT_create()

file = input('Enter the file name: ')
if not os.path.exists(file):
    print("File not found")
    exit()
    
video = cv2.VideoCapture(file)
ok, frame = video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break
    ok, bbox = tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # ESC
        break

