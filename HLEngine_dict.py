#author:Akhil P Jacob
#HLDynamic-Integrations
from PyDictionary import PyDictionary

def dict(param):
    try:
        dictionary = PyDictionary()
        a = dictionary.meaning(param)
        print(a)
    except:
        return ("HLEngine:Error in executing dict")

