import numpy as np
from PIL import ImageGrab
import cv2
import time

start_time = time.time()
while(True):
    #Captures the contents displayed on the monitor at the specified bbox=(w0, h0, w, h)
    printscreen_pil = ImageGrab.grab(bbox=(0,40, 1024, 768))

    #Conver screen to a Numpy Array since that is the type needed for cv2
    screen = np.array(printscreen_pil)
    print('Loop too {} seconds'.format(time.time() - start_time))
    start_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
