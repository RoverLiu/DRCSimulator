import simulatorInterface
import cv2
import numpy as np

def controller(image):
    #cv2.putText(image,"Hello World!!!", (10,10), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    # Write some Text

    font                   = cv2.FONT_HERSHEY_SIMPLEX
    org = (10,500)
    fontScale              = 1
    fontColor              = (0,255,255)
    lineType               = 2

    image = cv2.putText(np.unit8(image),'Hello World!', 
        org, 
        font, 
        fontScale,
        fontColor,
        lineType)

    cv2.imshow("car view",image)
    cv2.waitKey(1)
    
    controlCommand={}
    controlCommand["speed"]=100
    controlCommand["steer"]=0.5
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()