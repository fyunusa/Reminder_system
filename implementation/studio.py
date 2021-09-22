import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()      

with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    
    user_statement =  r.recognize_google(audio)
    print("You said " + user_statement)

    searched_string = "upcoming classes"

    if searched_string in user_statement:
        print("the string you searched for is in the statement that was just being made......" + searched_string) 

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

