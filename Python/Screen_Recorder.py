  
from tkinter import Frame
import numpy as np
from PIL import ImageGrab
import cv2
vc=cv2.VideoWriter_fourcc(*"XVID")
size=(ImageGrab.grab()).size
vw=cv2.VideoWriter("Record.mp4",vc,5.0,size)
while True:
    nparr=np.array(ImageGrab.grab())
    frame=cv2.cvtColor(nparr,cv2.COLOR_BGR2RGB)
    cv2.imshow("Recoder",frame)
    vw.write(nparr)
    if cv2.waitKey(1)==27:
        break
vw.release()
cv2.destroyAllWindows