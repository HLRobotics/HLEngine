#author:Akhil P Jacob
#HLDynamic-Integrations
import wikipedia


def wiki(param):
    try:
        return(wikipedia.summary(param))
    except:
        return ("HLEngine:error in executing wiki....")



