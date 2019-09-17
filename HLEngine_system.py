#@author:Akhil P Jacob
#HLRobotics & Automation

from xml.dom import minidom
def sysArch(question):
    mydoc = minidom.parse('HL_HiveMind/HL_HiveMind_Hub.xml')
    sources = mydoc.getElementsByTagName('source')
    first, *middle, last = question.split()
    for elem in sources:
        x = elem.firstChild.data
        if (x == str(last)):
            checker = int(elem.attributes['name'].value)
            ans = (sources[checker].firstChild.data)
            print("HLEngine:"+ans)
            return(str(ans))


