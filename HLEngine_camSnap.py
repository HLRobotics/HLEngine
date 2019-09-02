#@author:Akhil P Jacob
#HLRobotics-Automation
import cv2
def camSnap(location):
    try:
        camera = cv2.VideoCapture(0)
        while True:
            return_value, image = camera.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('HLEngine_camSnap', gray)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                cv2.imwrite(location, gray)
                break
        camera.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine:Camera not connected")

def filter(filter,cam,frameName):
    try:
        cap = cv2.VideoCapture(cam)

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(filter)
        framer=frameName
        while (True):

            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            net = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                # flags = cv2.CV_HAAR_SCALE_IMAGE
            )

            #print(format(len(net)))
            # print (len(faces))
            if (len(net) >= 2):
                return ("found 2 eyes")



            # Draw a rectangle around the faces
            for (x, y, w, h) in net:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow(framer, frame)
            if cv2.waitKey(1) & 0xFF == ord('x'):
                break


        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine: An issue with camera or params")





