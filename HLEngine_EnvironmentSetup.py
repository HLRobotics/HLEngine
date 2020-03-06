#@author:Er.Akhil P Jacob
#HLEngine Environmental settings
import subprocess
import sys
def setup_libraries():
    from xml.dom import minidom
    mydoc = minidom.parse('payload_setup.xml')
    payload = mydoc.getElementsByTagName('payload')        
    for elem in payload:
        print(elem.firstChild.data)
        package = str(elem.firstChild.data)
        try:
            print("HLEngine : Commencing installation......")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except:
            print("HLEngine: Installation failed....")


def setup_libraries_linuxVersion():
    from xml.dom import minidom
    mydoc = minidom.parse('payload_setup.xml')
    payload = mydoc.getElementsByTagName('payload')        
    for elem in payload:
        print(elem.firstChild.data)
        package = str(elem.firstChild.data)
        try:
            print("HLEngine : Commencing installation......")
            subprocess.check_call([sys.executable, "-m", "pip3", "install", package])
        except:
            print("HLEngine: Installation failed....")
