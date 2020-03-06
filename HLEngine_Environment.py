#@author:Akhil P Jacob
#HLRobotics-Automation
import git
import cv2
import subprocess
import sys

def update():
    try:
        # git.Git("Updates/").clone("https://github.com/HLRobotics/QBee.git")
        # print("done downloading .....")
        print("HLEngine:updating ......")
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


def install_package_windows(package):
    try:
        print("HLEngine : Commencing installation......")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        print("HLEngine: Installation failed....")


def install_package_linux(package):
    try:
        print("HLEngine : Commencing installation......")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", package])
    except:
        print("HLEngine: Installation failed....")


            


