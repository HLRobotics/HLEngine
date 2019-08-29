#@author:Akhil P Jacob
#HLRobotics-Automation

from gtts import gTTS
import pygame



def saveAudio(param,location):
    try:
        mytext = param
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(location)
    except:
        return ("HLEngine:saveAudio issue detected")


def playAudio(location):
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(location)
        pygame.mixer.music.play()
        pygame.event.wait()
    except:
        return ("HLEngine:playAudio issue detected")


"""def readAudio(param):
    try:
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        engine.say(param)
        engine.runAndWait()
    except:
        return ("HLEngine:readAudio issue detected")


"""

