import cv2

# Dictionary of Trackers that can be used

# TrDict = {
#     'csrt': cv2.TrackerCSRT_create(),
#     'kcf': cv2.TrackerKCF_create(),
#     'boosting': cv2.TrackerBoosting_create(),
#     'mil': cv2.TrackerMIL_create(),
#     'tld': cv2.TrackerTLD_create(),
#     'medianflow': cv2.TrackerMedianFlow_create(),
#     'mosse': cv2.TrackerMOSSE_create()
# }

# Tracker object initialised

# tracker = TrDict['csrt'] 
tracker = cv2.TrackerMIL_create()
vid = cv2.VideoCapture(r'Sources/sample1.mp4')

ret, frame = vid.read()
# frame = cv2.resize(frame, (2*328, 2*216))

cv2.imshow('Frame',frame)
bbox = cv2.selectROI('Frame',frame)
tracker.init(frame,bbox)

while True:
    ret, frame = vid.read()
    if not ret:
        break
    (success, box) = tracker.update(frame)
    if success:
        (x,y,w,h) = [ int(a) for a in box]

        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),2)
    
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()