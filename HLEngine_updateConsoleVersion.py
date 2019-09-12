import git
import cv2

def update():
    try:
        # git.Git("Updates/").clone("https://github.com/HLRobotics/QBee.git")
        # print("done downloading .....")

        git_dir = "../HL_Engine/"
        g = git.cmd.Git(git_dir)
        g.pull()
        print("HLEngine:done updating ......")
        img = cv2.imread('HLEngine.png')
        cv2.imshow('HLEngine updates', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except:
        return("HLEngine:cannot connect to cloud")

