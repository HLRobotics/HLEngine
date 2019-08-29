#@author:Akhil P Jacob
#HLRobotics-Automation
import cv2
import pyzbar.pyzbar as pyzbar
cap = cv2.VideoCapture(0)


def qrTech():
    try:
        print("HLEngine:press x to close")
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                user = str(obj.data)
                print(user)
                return (user)
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (0, 0, 255), 3)


            cv2.imshow("HLEngine QRScanner ", frame)

            if cv2.waitKey(1) & 0xFF == ord('x'):
                print("HLEngine:/> closing ...OK")
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        return ("HLEngine:Error in executing qrTech.....")
