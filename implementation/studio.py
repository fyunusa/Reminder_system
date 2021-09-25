import speech_recognition as s_r

print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
print(r.recognize_google(audio)) #to print voice into text

# get audio from the microphone                                                                       
        r = sr.Recognizer()      

        with sr.Microphone() as source:                                                                       
            print("Speak i can hear you:")                                                                                   
            audio = r.listen(source)   

        try:
            
            user_statement =  r.recognize_google(audio)
            print("You said " + user_statement)

            searched_string = "upcoming classes"

            if searched_string in user_statement:
                print("the string you searched for is in the statement that's just being made......" + searched_string) 

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))