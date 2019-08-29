#@author:Akhil P Jacob
#HLRobotics-Automation
import cv2
def camSnap(param):
    try:
        camera = cv2.VideoCapture(0)
        while True:
            return_value, image = camera.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('HLEngine_camSnap', gray)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                cv2.imwrite(param, gray)
                break
        camera.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine:Camera not connected")



