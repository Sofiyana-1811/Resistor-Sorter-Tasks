
import cv2
from datetime import datetime

rec=False
show=True
rec_start_time=0


def clicc(event,x,y,flags,params):
    global show
    global rec
    global rec_start_time
    if event==cv2.EVENT_RBUTTONDOWN:
        if ((datetime.now().second-rec_start_time)>=5) and (rec==True):
            if x<=507 and x>=407 and y<=255 and y>=215:
                show=False
                rec=False


cap = cv2.VideoCapture('rr.avi')#change to 0 for webcam
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #854
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #480
x,y=int(width/2),int(height/2)



fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter('output.avi', fourcc, fps, (int(width),int(height)))


while(show):
    ret, frame = cap.read()
    if ret==True:
        
        if cv2.waitKey(1) & 0xFF == ord('i'):
            rec_start_time=datetime.now().second
            rec=True
        
        if ((datetime.now().second-rec_start_time)>=5)and(rec==True):
            frame=cv2.rectangle(frame, (x-20, y-25), (x+80, y+15), (0, 0, 255), -1)
            frame=cv2.putText(frame, 'IPSITA', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.69, (255, 255, 255), 2)

        if rec:
            out.write(frame.astype('uint8'))
        
        cv2.imshow('frame',frame)
        cv2.setMouseCallback('frame', clicc)
        
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()