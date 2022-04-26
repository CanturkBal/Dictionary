from multiprocessing import set_forkserver_preload
import pyttsx3 #text data to speech

import speech_recognition as src #pip install Speech_Recognition == mic to text







from PyDictionary import Pydictionary

engine = pyttsx3.init() #creating the engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommandmic():
    r= src.Recognizer()
    with src.Microphone() as source:#opening mic
        print("listening...") #saving the voice to audio variable
        r.pause_threshold  =1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("please say that again")
        
        return "None"
    return query

dict = PyDictionary()
try:
  
# meaning of "python"
  meaning = dict.meaning(query)
  speak(meaning)
  print(meaning)
except KeyboardInterrupt:
  print("quitted succesfully")
