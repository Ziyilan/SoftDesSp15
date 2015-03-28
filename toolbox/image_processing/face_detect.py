""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/zlan/haarcascade_frontalface_alt.xml')
kernel = np.ones((40,40),'uint8')

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		#cv2.rectangle(frame,(x+w,y+h),(x+w,y+h),(0,0,255))
		cv2.circle(frame,(x+w/4, y+h/4), 50, (0,0,0), -1)
		cv2.circle(frame,(x+3*w/4, y+h/4), 50, (0,0,0), -1)
		cv2.circle(frame,(x+w/2, y+7*h/12), 20, (0,0,255), -1)
		cv2.line(frame,(x+w/4,y+11*h/12),(x+w/2,y+3*h/4),(255,0,0),10)
		cv2.line(frame,(x+w/2,y+3*h/4),(x+3*w/4,y+11*h/12),(255,0,0),10)



# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()