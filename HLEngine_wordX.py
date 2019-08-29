#@author:Akhil P Jacob
#HLRobotics-Automation

def FW(param):
    try:
        sent=str(param)
        first, *middle, last = sent.split()
        #print(first, last)
        return(first)
    except:
        return("HLEngine:Error in excuting FW.....")

def EW(param):
    try:
        sent=str(param)
        first, *middle, last = sent.split()
        #print(first, last)
        return(last)
    except:
        return ("HLEngine:error in executing EW....")

