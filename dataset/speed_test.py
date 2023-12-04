import numpy as np
import cv2
import time 

cap = cv2.VideoCapture(0)

start_time = time.time()
end_time = start_time
elapsed_time = 1

font = cv2.FONT_HERSHEY_SIMPLEX
  
org = (50, 50)
fontScale = 1  
color = (255, 0, 0)
thickness = 2
   
while(True):

    start_time = time.time()
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame

    cv2.putText(gray, str(1 / elapsed_time) + "fps", org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    end_time = time.time()
    elapsed_time = end_time - start_time


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()