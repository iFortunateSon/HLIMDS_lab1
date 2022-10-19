# import the opencv library
import cv2
vid = cv2.VideoCapture(0)

WIDTH = 640 / 4
HEIGHT = 480 / 4

vid.set(3, WIDTH)  # set Width
vid.set(4, HEIGHT)  # set Height

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


