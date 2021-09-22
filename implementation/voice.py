import speech_recognition as sr

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))

# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
    
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()