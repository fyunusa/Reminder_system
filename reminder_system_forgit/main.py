from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.gridlayout import MDGridLayout
#----------------#----------------#-------------#------------#
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
#----------------#----------------#-------------#------------#
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionItem
#----------------#----------------#-------------#------------#
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.picker import MDTimePicker,MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Rectangle

#----------------#----------------#-------------#------------#
import os
import sys
import schedule
import datetime
import re
import threading
import time
from datetime import date
from dateutil import parser
import speech_recognition as sr
import shutil
import pyttsx3
import pyjokes
from pathlib import Path
import random
from playsound import playsound
import pyaudio
import wave
import random
# from pynput import keyboard

#----------------#----------------#-------------#------------#
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.factory import Factory

#----------------#---------Voice-------#-------------#------------#
from kivy.resources import resource_add_path, resource_find

#----------------#------------json's----#-------------#------------#
store = JsonStore('user_data.json')

#----------------#---------Kv's-------#-------------#------------#
Builder.load_file("home.kv")
Builder.load_file("login.kv")
Builder.load_file("sign_up.kv")
Builder.load_file("calendar.kv")
Builder.load_file("Ttable.kv")
Builder.load_file("scheduler.kv")
Builder.load_file("user_menu.kv")




class Home_page(Screen):


    def pressed_button_login(self, instance):
        username = self.ids.menu_username.text
        password = self.ids.menu_password.text

        if store.exists(username):
            users_password = store.get(username)['password']
            if password == users_password:
                reminder_app.screen_manager.current = "UserMenu"
            else:
                self.ids.menu_password.text = "invalid password"      
        else:
            self.ids.menu_username.text = "invalid username"
        
        # self.ids.menu_username.text = ""
        # self.ids.menu_password.text  = ""
    
    #----------------------------------------------------------------------------#
    def pressed_button_UMenu(instance):
        reminder_app.screen_manager.current = "UserMenu"
        caller = UserMenu_page()
        caller.exam_date()
        caller.slide_it()
#----------------------------------------------------------------------------#
    def pressed_button_SignUp(instance):
        reminder_app.screen_manager.current = "Sign_up"
#----------------------------------------------------------------------------#
    def pressed_button_Verify(instance):
        reminder_app.screen_manager.current = "verify"
#----------------------------------------------------------------------------#
    def pressed_button_Login(instance):
        reminder_app.screen_manager.current = "Login"
#----------------------------------------------------------------------------#
    def pressed_button_Home(instance):
        reminder_app.screen_manager.current = "Home"
#----------------------------------------------------------------------------#    
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        print(f"this is the screen it's requesting {screen_name}")
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass

    #----------------------------------------------------------------------------#

    def slide_images(self):        
       
    #------------------------###############-----------------------------------#
        
        path = './carousel_images_Home/'
        dir_list = os.listdir(path)
        tile_images_list = dir_list

        for i in range(0, len(tile_images_list), 1):
            src = path+tile_images_list[i]
            image = Image(source=src, allow_stretch=True)
            self.ids.home_carousel.add_widget(image)

        Clock.schedule_interval(self.ids.home_carousel.load_next,5)

        self.ids.slide_img.min = 0
        self.ids.slide_img.max = len(tile_images_list)
        self.ids.slide_img.step = 1     

    def slide_carousel(self):

    #----------------#------slider parameters------------#------------#

        read_quote_file = open('./inspirational_quotes.txt', 'r')
        read_advantage_file = open('./advan.txt', 'r')
        quotes = read_quote_file.readlines()
        advantages = read_advantage_file.readlines()
    #------------------------###############-----------------------------------#

        # for i in range(len(quotes)):
            # if i%2 == 1:
            #     i = i + 1
            # elif i%2 != 1: 
            #     i = i
        #     if self.ids.slide_img.value  == i:
        #         if i < len(quotes):
        #             quote_length = len(quotes[i])
        #             self.ids.quote_widget.text = quotes[i]


    #------------------------###############-----------------------------------#
        for i in range(0, 100, 1):

            if i%2 == 1:
                i = i + 1

            elif i%2 != 1: 
                i = i

            if i < len(quotes):
                Label1 =  Label(text= quotes[i]+'\n'+quotes[i+1], size=(700, 400),padding_y=20,text_size=(700,None),padding_x=20,halign='center',valign='middle')
                
                self.ids.home_carousel_label1.add_widget(Label1)

            else:
                i = 0

    #------------------------###############-----------------------------------#
        for i in range(0, 100, 1):

            if i < len(advantages):
                label2 =  Label(text= advantages[i], size=self.size,text_size=(700,None),padding_y=20,padding_x=20,halign='center',valign='middle')
                self.ids.home_carousel_label2.add_widget(label2)

            else:
                i = 0

    #------------------------###############-----------------------------------#
        Clock.schedule_interval(self.ids.home_carousel_label1.load_next,20)
        Clock.schedule_interval(self.ids.home_carousel_label2.load_next,20)
    #------------------------###############-----------------------------------#

        # for i in range(len(advantages)):
        #     if self.ids.slide_img.value  == i:
        #         if i < len(advantages):
        #             advantage_length = len(advantages[i])
        #             self.ids.advantage_widget.text = advantages[i]
    
    pass
#----------------------------------------------------------------------------#

class kira:
   

    def talk_kira(instance):
        kira_introduction = """My name is Kira, 
                i'll be your personal assistant for the main time """

        Kira_knowing_you = """Do you mind introducing yourself also ?, 
                Can i know you ?"""

        kira_asking_if_you_need_help = """How may I be of help to you ?,
                Do you need help in searching for your assignments ?,
                Do you want to know about your class schedule ?,
                i'm available all time feel free to talk to me ok ?"""

        # self.other_task_kira()
#----------------------------------------------------------------------------#
    def speak(audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        # -----------voices[1].id is for female voice and voices[0].id is for male-----------#
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 180)

        engine.say(audio)
        engine.runAndWait()
#----------------------------------------------------------------------------#
    @staticmethod
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
           kira.speak("Good Morning !")

        elif hour>= 12 and hour<18:
           kira.speak("Good Afternoon !")

        else:
            kira.speak("Good Evening !")
#----------------------------------------------------------------------------#
    @staticmethod
    def usrname():
        kira.speak("What should i call you sir")
        uname = kira.takeCommand()

        kira.speak("Welcome {0}".format(uname))
        
        # kira.speak("Welcome {0}".format(uname))
        
        kira.speak("How can i Help you ?")
#----------------------------------------------------------------------------#
    @staticmethod
    def takecmd_note_option():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            kira.speak(""" will you like to hear your note now ?""")
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=5)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in')
            print(query)
        
        except Exception as e:
          
            kira.speak("""Sorry i can't process your command.
            verily i can't help with your note""")
            return "None"

        return query
#----------------------------------------------------------------------------#

    @staticmethod
    def takeCommand_date():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            kira.speak(""" Should i include date to your note which i'm about to write ? """)
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=5)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in')
            print(query)
        
        except Exception as e:
          
            kira.speak("""Sorry i can't process your command.
            verily i can't help with your note""")
            return "None"

        return query
#----------------------------------------------------------------------------#

    @staticmethod
    def takeCommand_note():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            kira.speak(""" i'm with you,
            you can start dictating your note so i'll listen to you for 30 seconds each """)
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=30)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in')
            print(query)
        
        except Exception as e:
          
            kira.speak("""Sorry i can't process your command.
            verily i can't help with your note""")
            return "None"

        return query
#----------------------------------------------------------------------------#
    @staticmethod
    def takeCommand():

        r = sr.Recognizer()

        with sr.Microphone() as source:
            kira.speak(""" Hi,
             i'm with you, 
             what will you like me to help you with ? """)
            r.pause_threshold = 1
            audio = r.listen(source,phrase_time_limit=10)

           
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language ='en-in')
            print(query)
        
        except Exception as e:
          
            kira.speak("Sorry i can't process your command.")
            return "None"

        return query
    
#----------------------------------------------------------------------------#
    @staticmethod
    def other_task_kira():

        assname = 'kira'
        count = 0
        while count < 3:
            count += 1


            query = kira.takeCommand().lower()
            print('querying in other task is {0}'.format(query))

            """All the commands said by user will be
                stored here in 'query' and will be
                converted to lower case for easily
                recognition of command"""
        #--------------------------------------------#
    
            if count ==3:
                kira.speak("""i will like to take some rest now,
                Do you still have other things which you need me to help you with ?""")
                if "yes" in query:
                    count = 0
                else:
                    count = count
        #--------------------------------------------#

            if  'assignment' in query:
               kira.speak('Searching for scheduled assignment')
               instatiate = UserMenu_page()
               kira.speak(instatiate.schedule_assignment_pop())
               print(instatiate.schedule_assignment_pop())
        #--------------------------------------------#

            elif 'course' in query:
                kira.speak('Searching for scheduled courses')
                instatiate = UserMenu_page()
                kira.speak(instatiate.schedule_pop())
                print(instatiate.schedule_pop())
        #--------------------------------------------#

            elif 'open timetable' in query:
                # kira.speak("Thanks for your time")
                kira.speak("you'll be directed to the records page shortly")
                # TimeTable_page.pressed_button_record("TimeTable")
                return TimeTable_page.clicker_button()

            elif 'open assignments' in query:
                kira.speak("you'll be directed to the records page shortly")
                # TimeTable_page.pressed_button_record("TimeTable")
                return TimeTable_page.clicker_button2()


            elif 'class' in query or 'classes' in query:
                kira.speak('Searching for scheduled classes...')
                instatiate = UserMenu_page()
                kira.speak(instatiate.schedule_pop())
                print(instatiate.schedule_pop())

            elif 'exam' in query:
                kira.speak('Searching for scheduled  exams...')
                kira.speak('my knowledge is limited for now, just few updates and adjustments then hopefully i will be able to handle your request in the future')

            elif 'test' in query:
                kira.speak('Searching for scheduled test...')
                kira.speak('my knowledge is limited for now, just few updates and adjustments then hopefully i will be able to handle your request in the future')

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                kira.speak(f"the time is {strTime}")

            elif 'how are you' in query:
                kira.speak("I am fine, Thank you")
                kira.speak("How are you too ?")
                kira.speak("Do you have anything for me ?")

            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname2 = query

            elif "change your name" in query:
                kira.speak("What would you like to call me, Sir ")
                assname = kira.takeCommand()
                kira.speak("Thanks for naming me")

            elif "what's your name" in query:
                kira.speak(f"My creator call me {assname}")
                # kira.speak(assname)
                #print("My friends call me", assname)

            elif 'exit' in query or  "stop listening" in query:
                kira.speak("Thanks for giving me your time")
                break

            elif "who made you" in query or "who created you" in query:
                kira.speak("I have been created by Dr. Junior")
                
            elif 'joke' in query:
                kira.speak(pyjokes.get_joke())
            
            elif "who am i" in query:
                kira.speak("If you talk then definitely your human.")

            elif "why you came to existence" in query:
               kira.speak("Thanks to my creator Dr. Junior further It's a secret")
            
            elif "who are you" in query:
                kira.speak("I am your virtual assistant created by Dr. Junior a final year student of university of ibadan ")

            elif 'reason for you' in query:
                kira.speak("I was created as a Minor project by Dr. Junior to help reduce forgetfullness in students ")

            elif 'sign up' in query:
                kira.speak("Thanks for your time")
                kira.speak("you'll be directed to the sign up page shortly")
                return Home_page.pressed_button_SignUp("Sign_up")
               
            elif 'verification page' in query:
                kira.speak("Thanks for your time")
                kira.speak("you'll be directed to the verification page shortly")
                return Home_page.pressed_button_Verify("verify")
                
            elif 'homepage' in query:
                kira.speak("Thanks for your time")
                kira.speak("you'll be directed to the homepage page shortly")
                return Home_page.pressed_button_Home("Home")
            
            elif "write a note" in query:
                kira.speak("What should i write, sir")
                file = open('kira_note.txt', 'w')
                snfm =kira. takeCommand_date()
                if 'yes' in snfm or 'sure' in snfm:
                    dt = datetime.datetime.now()
                    curntime = dt.strftime("%H:%M:%S")
                    today = date.today()
                    note = kira.takeCommand_note()
                    file.write(f"this note is written on {today} and time {curntime}")
                    file.write(" :- \n")
                    file.write(note)
                    kira.speak("ok, thank you, it's 30 seconds already and i'm done listening to you ")
                    option = kira.takecmd_note_option()

                    if "yes" in option:
                        kira.speak("Preparing to read your note according to my knowledge")
                        file = open("kira_note.txt", "r")
                        content = file.read()
                        print(content)
                        kira.speak(content)

                    else:
                        kira.speak("ok bye, catch up with you later...")

                else:
                    note = kira.takeCommand_note()
                    file.write(note)

            elif "read the note" in query or 'read my note' in query or 'show notes' in query or 'read notes' in query:
                kira.speak("Preparing to read your note according to my knowledge")
                file = open("kira_note.txt", "r")
                content = file.read()
                print(content)
                kira.speak(content)

            elif "kira listen to me" == query:
                kira.wishMe()
                kira.speak("kira 1 point o in your service Sir")
                kira.speak(assname)
            
            elif "thank you" in query:
                kira.speak("Bye, catch up with you later...")

            else:
                kira.speak("I don't seem to understand you ")


#-----------------------------------------------------------#

class Login_page(Screen):

    def pressed_button_Home(self, instance):
        reminder_app.screen_manager.current = "Home"
    
    def pressed_button_SignUp(self, instance):
        reminder_app.screen_manager.current = "Sign_up"
    
    def pressed_button_Verify(self, instance):
        reminder_app.screen_manager.current = "verify"

    def login_logger(self):
        self.ids.welcome_label.text = f'welcome {self.ids.user.text } !'
        
        with open("previous_details.txt", "w") as f:
            f.write(f"{self.ids.user.text},{self.ids.password.text }")
        
        reminder_app.screen_manager.current = "UserMenu"

    def login_clear(self):

        self.ids.welcome_label.text = "welcome"
        self.ids.user.text = ""
        self.ids.password.text = ""
    
    #----------------------------------------------------------------------------#    
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        print(f"this is the screen it's requesting {screen_name}")
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass

    

    pass
#-----------------------------------------------------------#
#-----------------------------------------------------------#
class UserMenu_page(Screen):
    def tile_change(self):

        path = './carousel_images_Umenu/'
        dir_list = os.listdir(path)
        tile_images_list = dir_list
        read_advantage_file = open('./advan.txt', 'r')
        uses = read_advantage_file.readlines()

        i = random.randrange(len(tile_images_list))
        ib = random.randrange(len(uses))
        self.ids.umenu_tile1.source = path+tile_images_list[i]
        self.ids.umenu_tile1.text = uses[ib]

        j = random.randrange(len(tile_images_list))
        jb = random.randrange(len(uses))
        self.ids.umenu_tile2.source = path+tile_images_list[j]
        self.ids.umenu_tile2.text = uses[jb]
        
        k = random.randrange(len(tile_images_list))
        kb = random.randrange(len(uses))
        self.ids.umenu_tile3.source = path+tile_images_list[k]
        self.ids.umenu_tile3.text = uses[kb]

#-----------------------------------------------------------#
    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"

#-----------------------------------------------------------#
    def exam_date(self):
        if store.exists('Exam'):
            exam_date = store.get('Exam')['Due_date']
            print(f"this is the exam date: {exam_date}")

            today = date.today()
            today = today.strftime("%Y-%m-%d")

            days_diff = self.days_between(exam_date,today)

            self.welcome = "Scheduled Exam Starts In Next"
            self.ids.user_menu_widget1.text = "Scheduled Exam Starts In Next"
            self.ids.user_menu_widget2.text = str(days_diff) + "\nDays"
        else:
            self.ids.user_menu_widget1.text = "Exam Date not Scheduled yet"
            self.ids.user_menu_widget2.text = "0\nDays"

        return  self.ids.user_menu_widget1.text 
        
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        print(f"this is the screen it's requesting {screen_name}")
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass

#-----------------------------------------------------------#
    def pressed_button_scheduler(self, instance):
        reminder_app.screen_manager.current = "Scheduler"

#-----------------------------------------------------------#
    def pressed_button_calender(self, instance):
        reminder_app.screen_manager.current = "Calendar"

#-----------------------------------------------------------#
    def pressed_button_record(self, instance):
        reminder_app.screen_manager.current = "TimeTable"

#-----------------------------------------------------------#
    def pressed_button_kira(self):
        caller = kira()
        caller.other_task_kira()

#-----------------------------------------------------------#
    def slide_it(self):

        scheduler = self.schedule_pop()
        scheduler2 = self.schedule_others_pop()
        #----------------#------slider parameters------------#------------#
       
        for i in range(0, 100, 1):

            if i < len(self.popupData):
                L = Label(text=self.popupData[i], size=(730, 400),text_size=(700,None),padding_y=20,padding_x=20,halign='center',valign='middle')
                self.ids.schedule_carousel.add_widget(L)

            else:
                i = 0

        for i in range(0, 100, 1):

            if i < len(self.popupData_Others):
                L2 =  Label(text= self.popupData_Others[i], size=(730, 400),text_size=(700,None),padding_y=20,padding_x=20,halign='center',valign='middle')
                self.ids.schedule_carousel2.add_widget(L2)

            else:
                i = 0

        Clock.schedule_interval(self.ids.schedule_carousel.load_next,15)
        Clock.schedule_interval(self.ids.schedule_carousel2.load_next,10)

        return self.ids.schedule_carousel
                
#-----------------------------------------------------------#
    def time_converter(self,s):
        s = ''

        if s[-2:] == "AM" or s[-2:] == "am" :

            if s[:2] == '12':
                a = str('00' + s[2:8] )
            else:
                a = s[:-2]

        else:
            if s[:2] == '12':
                a = s[:-2]
            else:
                a = str(int(s[:2]) + 12) + s[2:8]
            
        return a

#------------------------###############-----------------------------------#

    def days_between(self,d1, d2):
        d1 = parser.parse(d1)
        d2 = parser.parse(d2)
        diff = d1 - d2
        return diff.days
#-----------------------------------------------------------#
    def schedule_assignment_pop(self):
        today = date.today()
        today = today.strftime("%Y-%m-%d")

        for item in store.find(type="Assignment"):
            course_title = store.get(item[0])['Title']
            course_code = store.get(item[0])['Code']
            Question = store.get(item[0])['Question']
            assign_date = store.get(item[0])['Assign_date']
            due_date = store.get(item[0])['Due_date']

            days_diff = self.days_between(due_date,today)
            print(days_diff)
            if days_diff < 0:
                statement = "the schedule assignment is due already"
            else:
                statement = f"you have {course_title} assignment which is due in next {days_diff} days"

            return statement

#-----------------------------------------------------------#
    def schedule_others_pop(self):
        self.popupData_Others = []
        category = ['Schedule other task', 'Exam', 'Test', 'Special_Days', 'Special_Week', 'Dinner', 'Cultural night']
        for catg in category:
           for item in store.find(type=catg):
                # taskType = store.get(item[0])['type']
                task_name = store.get(item[0])['task_name']
                Note = store.get(item[0])['note']
                # Assign_Date = store.get(item[0])['Assign_date']
                Due_date = store.get(item[0])['Due_date']

                processedData_others = f"Schedule {task_name} coming up {Due_date} having spcl note {Note}\n"
                self.popupData_Others.append(processedData_others)
        
#-----------------------------------------------------------#
    def schedule_pop(self):
        summon_popup = Factory.pop()
        #-----------this will open the popup box--------#
        # response = summon_popup.open()
        dt = datetime.datetime.now()
        self.popupData = []
        containertime = []
        row_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
    #----------------#----------------#-------------#------------#
        current_day =  dt.strftime("%A")
        current_time = dt.strftime('%I:%M %p')
        current_time_hr = dt.strftime("%H:%M")
    
    #----------------#----------------#-------------#------------#
        for tableDay in row_days:
            if current_day.lower() == tableDay:
                for item in store.find(Day=tableDay):
                    course_code = store.get(item[0])['Code']
                    course_title = store.get(item[0])['Title']
                    self.start_time = store.get(item[0])['Start_time']
                    self.end_time = store.get(item[0])['End_time']

            #----------------#--------converting starttime to desired format--------#-------------#------------#
                    if self.start_time[-2:].lower() == "am" and self.start_time[:2] == "12":
                        new_starttime = "00" + self.start_time[2:8]

                    elif self.start_time[-2:].lower() == "am":
                        new_starttime = self.start_time[:-2]

                    elif self.start_time[-2:].lower() == "pm" and self.start_time[:2] == "12":
                        new_starttime = self.start_time[:-2]

                    else:
                        new_starttime = str(int(self.start_time[:2]) + 12) + self.start_time[2:5]

            #----------------#----------------#-------------#------------#
                    processedData = f"Upcoming {current_day} classes {course_code} which starts at {self.start_time} and ends at {self.end_time}\n"
            
            #----------------#------populate containers----------#-------------#------------#
                    self.popupData.append(processedData)
                    containertime.append(new_starttime)

            #----------------#----------------#-------------#------------#
            popupData_convert = ','.join(self.popupData)   
            summon_popup.ids.popuptext.text = popupData_convert

            #----------------#------popup title text------------#------------#
            headText = f"{0} Upcoming Scheduled Classes {current_day}\n"
            summon_popup.title = headText
        return  popupData_convert

#-----------------------------------------------------------#
    pass
#-----------------------------------------------------------#

class Sign_up_page(Screen):
#-----------------------------------------------------------#
    def signup_clear(self):

        self.ids.F_name.text = ""
        self.ids.S_name.text = ""
        self.ids.School.text = ""
        self.ids.Email.text = ""
        self.ids.Faculty.text = ""
        self.ids.Department.text = ""
#-----------------------------------------------------------#

    def pressed_button_login(self, instance):
        reminder_app.screen_manager.current = "Login"
#-----------------------------------------------------------#

    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Sign_up"
#-----------------------------------------------------------#
    def pressed_button_verify(self, instance):
        reminder_app.screen_manager.current = "verify"

    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass
#-----------------------------------------------------------#
    def pressed_button_submit(self):
#-----------------------------------------------------------#
        self.users_Fname = self.ids.F_name.text
        users_Sname = self.ids.S_name.text
        users_School = self.ids.School.text
        users_Email =  self.ids.Email.text
        users_Faculty = self.ids.Faculty.text
        users_Department = self.ids.Department.text
        
    #------------------------------------#

        store.put(
            self.users_Fname, 
            name = self.users_Fname,
            surname = users_Sname,
            school = users_School,
            email = users_Email,
            faculty = users_Faculty,
            department = users_Department
            )

        reminder_app.screen_manager.current = "verify"

    pass
#-----------------------------------------------------------#
#------------------------###############-----------------------------------#

class verify_page(Screen):

#-----------------------------------------------------------#

    def pressed_button_login(self, instance):
        reminder_app.screen_manager.current = "Login"
#-----------------------------------------------------------#

    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "verify"
    
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass
#-----------------------------------------------------------#
    def pressed_button_SignUp(self, instance):
        reminder_app.screen_manager.current = "Sign_up"
#-----------------------------------------------------------#
    def signup_clear(self):
        self.ids.username.text = ""
        self.ids.password1.text = ""
        self.ids.password2.text = ""
#-----------------------------------------------------------#
    def pressed_button_submit(self):
#-----------------------------------------------------------#
        users_username = self.ids.username.text
        users_password1 = self.ids.password1.text
        users_password2 = self.ids.password2.text
    #-----------------------------------------------------------#
        pass_compare = []
        pass_compare.append(users_password1)
        pass_compare.append(users_password2)
#-----------------------------------------------------------#
        if store.exists(users_username):
            text = 'The username {0} already exist'.format(users_username)
            self.ids.welcome_label.text = f' {text} !'

            reminder_app.screen_manager.current = "verify"

            self.ids.username.text = ""
            self.ids.password1.text = ""
            self.ids.password2.text = ""

        else:
            store.put(
            users_username,
            username = users_username,
            password = users_password2,
            )

            text = 'The username {0} is valid and verified'.format(users_username)
            self.ids.welcome_label.text = f'welcome {text} !'

            if pass_compare[0] == pass_compare[1]:
                password_text = 'password verified and correct: {0} '.format(pass_compare[0])
                self.ids.welcome_label2.text = f' {password_text} !'

                reminder_app.screen_manager.current = "Login"

            else:
                password_text = 'password mismatch: {0} not same as {1} '.format(pass_compare[0],pass_compare[1])
                self.ids.welcome_label2.text = f' {password_text} !'

                self.ids.password1.text = ""
                self.ids.password2.text = ""

                reminder_app.screen_manager.current = "verify"  
            #print(text)
#-----------------------------------------------------------#
    pass

#-----------------------------------------------------------#
#------------------------###############-----------------------------------#

class TimeTable_page(Screen):

#-----------------------------------------------------------#
    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
    
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass
#-----------------------------------------------------------#
    def pressed_button_record(self, instance):
        reminder_app.screen_manager.current = "TimeTable"
#-----------------------------------------------------------#
    def pressed_button_calendar(self, instance):
        reminder_app.screen_manager.current = "Calendar"
    #-----------------------------------------------------------#
    def pressed_button_scheduler(self, instance):
        reminder_app.screen_manager.current = "Scheduler"
#-----------------------------------------------------------#
    def pressed_button_usermenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def pressed_button_timetable(self, *args):
        self.TTable_layout = AnchorLayout()

        user_row_data=[]
        row_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        count = 1
        for days in row_days:
            for item in store.find(Day=days):
                json_data_collector = (
                    # The number of elements must match the length
                    # of the `column_data` list.
                    
                        count,
                        ( "alert-circle", [255 / 256, 165 / 256, 0, 1], store.get(item[0])['Day']),# for a row with icon
                        store.get(item[0])['Start_time'],
                        store.get(item[0])['End_time'],
                        store.get(item[0])['Code'],
                        store.get(item[0])['Title'],
                        store.get(item[0])['Units'],
                    )
                
                user_row_data.append(json_data_collector)
                count += 1

        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint = {'center_y': 0.5, 'center_x': 0.5},
            use_pagination = True,
            check = True,
            column_data=[
                ("No.", dp(20)),
                ("Day", dp(30), self.sort_on_day),
                ("Start Time", dp(30), self.sort_on_time ),
                ("End Time", dp(20)),
                ("Course Code", dp(30)),
                ("Course Title", dp(50), self.sort_on_title),
                ("Credit Units", dp(20)),
            ],
                
            row_data = user_row_data,
            # sorted_on="Time",
            # sorted_order="ASC",
            elevation = 20,
        )
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)
        return self.TTable_layout

#-----------------------------------------------------------#
    category = ['Schedule other task', 'Exam', 'Test', 'Special_Days', 'Special_Week', 'Dinner', 'Cultural night']
#-----------------------------------------------------------#
    def pressed_button_others_task(self, *args):
        self.TTable_layout = AnchorLayout()

        user_row_data=[]
        count = 1
        for catg in self.category:
            for item in store.find(type=catg):
                json_data_collector = (
                    count,
                    store.get(item[0])['type'],
                    store.get(item[0])['task_name'],
                    store.get(item[0])['note'],
                    store.get(item[0])['Assign_date'],
                    store.get(item[0])['Due_date'],
                   
                )
                
                user_row_data.append(json_data_collector)
                count += 1
        
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint = {'center_y': 0.5, 'center_x': 0.5},
            use_pagination = True,
            check = True,
            column_data=[
                ("No.", dp(20)),
                ("Schedule", dp(20)),
                ("Task", dp(40)),
                ("Note", dp(70)),
                ("Assigned Date", dp(20)),
                ("Event Date", dp(20)),
            ],
                
            row_data = user_row_data,
            elevation = 20,
        )
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)
        return self.TTable_layout

    #-----------------------------------------------------------#
    row_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    #-----------------------------------------------------------#
    def pressed_button_assignments(self, *args):
        self.TTable_layout = AnchorLayout()

        user_row_data=[]
        count = 1

        for item in store.find(type='Assignment'):
            json_data_collector = (
                # The number of elements must match the length
                # of the `column_data` list.
                
                    count,
                    ( "alert-circle", [255 / 256, 165 / 256, 0, 1], store.get(item[0])['Title']),# for a row with icon
                    store.get(item[0])['Code'],
                    store.get(item[0])['Question'],
                    store.get(item[0])['Assign_date'],
                    store.get(item[0])['Due_date'],
                )
            
            user_row_data.append(json_data_collector)
            count += 1
        
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint = {'center_y': 0.5, 'center_x': 0.5},
            use_pagination = True,
            check = True,

            column_data=[
                ("No.", dp(25)),
                ("Title", dp(35)),
                ("Course Code", dp(30)),
                ("Question", dp(70)),
                ("Assign Date", dp(30)),
                ("Due Date", dp(30)),
              
            ],

            row_data = user_row_data,
            # sorted_on="Time",
            # sorted_order="ASC",
            elevation = 20,
        )
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)
        return self.TTable_layout
    #-----------------------------------------------------------#
    def sort_on_col_units(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][3]
            )
        )
    #-----------------------------------------------------------#
    def sort_on_time(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-5].split(":")[0]) * 60,
                        int(l[1][-5].split(":")[1]),
                    ]
                ),
            )
        )
    #-----------------------------------------------------------#
    def sort_on_title(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-2]))
    #-----------------------------------------------------------#
    def sort_on_day(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-6]))
    #-----------------------------------------------------------#    
    def clicker_button(self):
        self.pressed_button_timetable()
    #-----------------------------------------------------------#
    def clicker_button2(self):
        self.pressed_button_assignments()
    #-----------------------------------------------------------#
    def clicker_button3(self):
        self.pressed_button_others_task()
    #-----------------------------------------------------------#
    def on_check_press(self, instance_table, current_row):
        """Called when the check box in the table row is checked."""
        self.instance = instance_table
        self.row_value = current_row
        # print(self.row_value)
#-----------------------------------------------------------#
    def check_data_deleter(self):
        self.instance
        self.row_value

        if self.row_value[1].lower() in self.row_days:
            value1 = self.row_value[4]
            value2 = self.row_value[1]
        else:
            value1 = self.row_value[2]
            value2 = self.row_value[4]

        self.key_2_del = str(value1)+str(value2)
        store.delete(self.key_2_del)
        
#-----------------------------------------------------------#

    pass
#-----------------------------------------------------------#
#------------------------###############-----------------------------------#

class scheduler_page(Screen):

    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Scheduler"
#-----------------------------------------------------------#
    def pressed_button_kira(self):
        kira.other_task_kira()
    #-----------------------------------------------------------#
    def pressed_button_Home(self,instance):
        reminder_app.screen_manager.current = "Home"
    
    def Spinner_page(self):
        screen_name = self.ids.spnr.text
        try:
            reminder_app.screen_manager.current = screen_name
        except Exception:
            pass
    #-----------------------------------------------------------#
    def pressed_button_usermenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def pressed_button_record(self, instance):
        reminder_app.screen_manager.current = "TimeTable"
#-----------------------------------------------------------#
    def pressed_button_calendar(self, instance):
        reminder_app.screen_manager.current = "Calendar"
#-----------------------------------------------------------#

    def slide_images(self, *args):
        #----------------#------slider parameters------------#------------#
        
        images_list = ['./images/convert1.jpg','./images/convert2.jpg','./images/convert3.jpg','./images/convert4.jpg','./images/convert5.jpg','./images/convert6.jpg']
        images_text_list = ['we do not forgive', 'we do not forget', 'we are unstoppable']
        
        read_quote_file = open('./inspirational_quotes.txt', 'r')
        # read_advantage_file = open('./advan.txt', 'r')
        quotes = read_quote_file.readlines()
        # advantages = read_advantage_file.readlines()

        self.ids.slide_img.min = 0
        self.ids.slide_img.max = len(images_list)
        self.ids.slide_img.step = 1

        
        for i in range(len(images_list)):
            if self.ids.slide_img.value  == i:
                self.ids.image_tite.source = images_list[i]
        
        for i in range(len(quotes)):
            if i%2 == 1:
                i = i + 1
            elif i%2 != 1: 
                i = i
            if self.ids.slide_img.value  == i:
                if i < len(quotes):
                    quote_length = len(quotes[i])
                    self.ids.quote_widget2.text = quotes[i]
                    # if quote_length <= 20:
                    #     self.ids.quote_widget.text = quotes[i]+quotes[i+1]
                    # else:
                    #     self.ids.quote_widget.text = quotes[i][0:20]+'\n'+quotes[i][20:40]+'\n'+quotes[i][40:60]+'\n'+quotes[i+1]

#-----------------------------------------------------------#
    def pressed_button_submit(self):
        #-----------------------------------------------------------#
        course_Day = self.ids.Day.text
        course_StartTime = self.ids.Start_time.text
        course_EndTime = self.ids.End_time.text
        course_code =  self.ids.course_code.text
        course_title = self.ids.course_title.text
        course_units = self.ids.credit_unit.text
        
        regexPattern = "(1[012]|[1-9]):"+ "[0-5][0-9](\\s)"+ "?(?i)(am|pm)"; 
        compiledPattern = re.compile(regexPattern)

        if re.search(compiledPattern, course_StartTime):
            if re.search(compiledPattern, course_EndTime):
                store.put(
                    course_code, 
                    day = course_Day.lower(),
                    course_StartTime = course_StartTime,
                    course_EndTime = course_EndTime,
                    code = course_code,
                    title = course_title,
                    unit = course_units
                    )
                
                self.ids.Day.text = ""
                self.ids.Start_time.text = ""
                self.ids.End_time.text = ""
                self.ids.course_code.text = ""
                self.ids.course_title.text = ""
                self.ids.credit_unit.text = ""

        else:
            self.ids.Start_time.text = ""
            self.ids.End_time.text = ""
            correct_user = "time format must end with am or pm"
            self.ids.Start_time.hint_text = correct_user

#-----------------------------------------------------------#
#--------------------widget for scheduling class---------------------------------------#
    
    def schedule_class(self):
#-----------------------------------------------------------#
        self.ids.schedule_something.clear_widgets()
        self.ids.schedule_something2.clear_widgets()
#-----------------------------------------------------------#
        self.Data1 = MDTextFieldRect(hint_text='Day e.g monday',text='')
        self.Data2 = MDTextFieldRect(hint_text='Start Time e.g 07:00:00 AM',text='')
        self.Data3 = MDTextFieldRect(hint_text='End Time e.g 09:00:00 PM',text='')
        self.Data4 = MDTextFieldRect(hint_text='Course Code e.g CSC 775',text='')
        self.Data5 = MDTextFieldRect(hint_text='Course Title" e.g Software Engineering',text='')
        self.Data6 = MDTextFieldRect(hint_text='Credit Units e.g 4C',text='')
#-----------------------------------------------------------#
        self.btn1 = Button(text='SUBMIT',font_size=12,size_hint=(0.4,1) )
        self.btn2 = Button(text='CLEAR',font_size=12,size_hint=(0.4,1) ) 

        self.btn1.bind(on_release=self.printer)
        self.btn2.bind(on_release=self.eraser)
#-----------------------------------------------------------#
        self.ids.schedule_something2.add_widget(self.btn1)
        self.ids.schedule_something2.add_widget(self.btn2)
#-----------------------------------------------------------#
        self.ids.schedule_something.add_widget(self.Data1)
        self.ids.schedule_something.add_widget(self.Data2)
        self.ids.schedule_something.add_widget(self.Data3)
        self.ids.schedule_something.add_widget(self.Data4)
        self.ids.schedule_something.add_widget(self.Data5)
        self.ids.schedule_something.add_widget(self.Data6)
        
        self.ids.schedule_something2.background_color = (255,99,71,0.5)
        self.ids.schedule_mom.background_color = (255,99,71,0.9)
        
#-----------------------------------------------------------#
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    category = ['Schedule other task', 'Exam', 'Test', 'Special_Days', 'Special_Week', 'Dinner', 'Cultural night']
#-----------------------------------------------------------#
    def printer(self,instance):
        
        try:
            Data_1 = self.Data1.text
        except Exception:
            Data_1 =  self.ids.assignment_scheduler.text
        
        print(f"this is printer data: {Data_1}")

        try:
            if Data_1.lower() in self.week_days:
                
                Day = self.Data1.text
                S_time = self.Data2.text
                E_time = self.Data3.text
                C_code =self.Data4.text
                C_title = self.Data5.text
                C_units = self.Data6.text
                unique_id = str(C_code)+str(Day)

                regexPattern = "(1[012]|[1-9]):"+ "[0-5][0-9]:"+"[0-5][0-9](\\s)"+ "?(?i)(am|pm)"; 
                compiledPattern = re.compile(regexPattern)

                if re.search(compiledPattern, S_time):
                    if re.search(compiledPattern, E_time):
                        store.put(
                            unique_id,
                            type='Class',
                            Day = Day.lower(),
                            Start_time = S_time,
                            End_time = E_time,
                            Code = C_code,
                            Title = C_title,
                            Units = C_units
                        )
                        self.Data1.text = ""
                        self.Data2.text = ""
                        self.Data3.text = ""
                        self.Data4.text = ""
                        self.Data5.text = ""
                        self.Data6.text = ""

                        self.Data1.hint_text = "Data Uploaded sucessfully"
                        self.Data2.hint_text = "Data Uploaded sucessfully"
                        self.Data3.hint_text = "Data Uploaded sucessfully"
                        self.Data4.hint_text = "Data Uploaded sucessfully"
                        self.Data5.hint_text = "Data Uploaded sucessfully"
                        self.Data6.hint_text = "Data Uploaded sucessfully"

                    kira.speak(f"""Wow, interesting,
                    this is kira, i can see you just made a class schedule for {Day},
                    which is {C_title},
                    i'll do my best to keep in touch ok ?
                    bye...""")

                else:
                    self.Data3.text = ""
                    self.Data2.text = ""
                    self.Data3.hint_text ="invalid time format try again, End Time e.g 09:00:00 PM"
                    self.Data2.hint_text ="invalid time format try again, Start Time e.g 07:00:00 AM"

        #----------------------------------------------------------------------------#
            elif Data_1 in self.category:

                category = self.ids.assignment_scheduler.text
                task_name = self.Data2.text
                spcl_note = self.Data3.text
                Assign_Date =self.Data4.text
                Due_Date =self.Data5.text
                unique_id = str(category)+str(Assign_Date)

                if self.ids.assignment_scheduler.text == "Schedule other task":

                    self.Data2.text = "must select one of the category above"
                
                else:
                    store.put(
                        category,
                        type = category, 
                        task_name = task_name,
                        note = spcl_note,
                        Assign_date = Assign_Date,
                        Due_date = Due_Date, 
                    )

                    
                    self.Data2.text = ""
                    self.Data3.text = ""
                    self.Data4.text = ""
                    self.Data5.text = ""

                    self.Data2.hint_text = "Data Uploaded sucessfully"
                    self.Data3.hint_text = "Data Uploaded sucessfully"
                    self.Data4.hint_text = "Data Uploaded sucessfully"
                    self.Data5.hint_text = "Data Uploaded sucessfully"

                    self.ids.assignment_scheduler.text = "Schedule other task"

                    kira.speak(f"""Wow, interesting,
                        this is kira, i can see you just made a schedule for {category},
                        that is {task_name},
                        which will be due on {Due_Date},
                        i'll do my best to keep in touch ok ?
                        bye...""")
        

        #----------------------------------------------------------------------------#
            else:

                Title= self.Data1.text
                C_code = self.Data2.text
                Question = self.Data3.text
                Assign_Date =self.Data4.text
                Due_Date =self.Data5.text
                unique_id = str(C_code)+str(Assign_Date)

                store.put(
                    unique_id,
                    type='Assignment', 
                    Title = Title,
                    Code = C_code,
                    Question = Question,
                    Assign_date = Assign_Date,
                    Due_date = Due_Date, 
                )
                self.Data1.text = ""
                self.Data2.text = ""
                self.Data3.text = ""
                self.Data4.text = ""
                self.Data5.text = ""

                self.Data1.hint_text = "Data Uploaded sucessfully"
                self.Data2.hint_text = "Data Uploaded sucessfully"
                self.Data3.hint_text = "Data Uploaded sucessfully"
                self.Data4.hint_text = "Data Uploaded sucessfully"
                self.Data5.hint_text = "Data Uploaded sucessfully"

                kira.speak(f"""Wow, interesting,
                    this is kira, i can see you just made a schedule for an Assignment {Title},
                    for {C_code},
                    which will be due on {Due_Date},
                    i'll do my best to keep in touch ok ?
                    bye...""")

        except Exception as e:
            pass

       
        
    #-----------------------------------------------------------#

    def eraser(self,instance):

        try:
            Data_1 = self.Data1.text
        except Exception:
            Data_1 =self.Data1

        if Data_1.lower() in self.week_days:
            self.Data1.text = ''
            self.Data2.text = ''
            self.Data3.text = ''
            self.Data4.text = ''
            self.Data5.text = ''
            self.Data6.text = ''

        elif Data_1 in self.category:
            self.Data2.text = ''
            self.Data3.text = ''
            self.Data4.text = ''
            self.Data5.text = ''

        else:
            self.Data1.text = ''
            self.Data2.text = ''
            self.Data3.text = ''
            self.Data4.text = ''
            self.Data5.text = ''
            
#-----------------------------------------------------------#
    def check_values(self, obj):
        self.ids.assignment_scheduler.text  = obj.text
        print(self.ids.assignment_scheduler.text)
        
#-----------------------------------------------------------#
    def schedule_others(self):
        
        self.ids.schedule_something.clear_widgets()
        self.ids.schedule_something2.clear_widgets()

        self.ids.schedule_mom.background_color =(255,99,225,0.1)
        self.ids.schedule_something.background_color = (255,99,71,0.5)

        btn1 = ToggleButton(text='Exam', group='task', on_press = self.check_values)
        btn2 = ToggleButton(text='Test', group='task', state='down', on_press = self.check_values)
        btn3 = ToggleButton(text='Special_Days', group='task', on_press = self.check_values)
        btn4 = ToggleButton(text='Special_Week', group='task', on_press = self.check_values)
       

        categories_layout = GridLayout(cols=6)
        categories_layout.add_widget(btn1)
        categories_layout.add_widget(btn2)
        categories_layout.add_widget(btn3)
        categories_layout.add_widget(btn4)
       
        self.Data2 = MDTextFieldRect(hint_text='Task Name e.g Deans cup',text='')
        self.Data3 = MDTextFieldRect(hint_text='Special Note',text='')
        self.Data4 = MDTextFieldRect(hint_text='Assigned Date e.g 10-05-2021',text='')
        self.Data5 = MDTextFieldRect(hint_text='Due Date e.g 10-05-2021',text='')
      
        self.btn1 = Button(text='SUBMIT',font_size=12,size_hint=(0.3,1) )
        self.btn2 = Button(text='CLEAR',font_size=12,size_hint=(0.3,1) ) 

        self.btn1.bind(on_release=self.printer)
        self.btn2.bind(on_release=self.eraser)
        
        self.ids.schedule_something2.add_widget(self.btn1)
        self.ids.schedule_something2.add_widget(self.btn2)

        self.ids.schedule_something.add_widget(categories_layout)
        self.ids.schedule_something.add_widget(self.Data2)
        self.ids.schedule_something.add_widget(self.Data3)
        self.ids.schedule_something.add_widget(self.Data4)
        self.ids.schedule_something.add_widget(self.Data5)
#-----------------------------------------------------------#
#--------------------widget for scheduling assignment---------------------------------------#
    def schedule_assignment(self):
        
        self.ids.schedule_something.clear_widgets()
        self.ids.schedule_something2.clear_widgets()

        self.ids.schedule_mom.background_color =(255,99,225,0.1)
        self.ids.schedule_something.background_color = (255,99,71,0.5)

        self.Data1 = MDTextFieldRect(hint_text='Course Title e.g CSC 542',text='')
        self.Data2 = MDTextFieldRect(hint_text='Course Code e.g CSC 775',text='')
        self.Data3 = MDTextFieldRect(hint_text='Question e.g Digital Logic Circuits & Diagrams',text='')
        self.Data4 = MDTextFieldRect(hint_text='Assigned Date e.g 10-05-2021',text='')
        self.Data5 = MDTextFieldRect(hint_text='Due Date e.g 10-05-2021',text='')
      
        self.btn1 = Button(text='SUBMIT',font_size=12,size_hint=(0.3,1) )
        self.btn2 = Button(text='CLEAR',font_size=12,size_hint=(0.3,1) ) 

        self.btn1.bind(on_release=self.printer)
        self.btn2.bind(on_release=self.eraser)
        
        self.ids.schedule_something2.add_widget(self.btn1)
        self.ids.schedule_something2.add_widget(self.btn2)

        self.ids.schedule_something.add_widget(self.Data1)
        self.ids.schedule_something.add_widget(self.Data2)
        self.ids.schedule_something.add_widget(self.Data3)
        self.ids.schedule_something.add_widget(self.Data4)
        self.ids.schedule_something.add_widget(self.Data5)
      
#-----------------------------------------------------------#
    pass
#-----------------------------------------------------------#
class Alarm:
    
#------------------------#######Return alarm time########-----------------------------------#
    
    def return_alarm_time(self):
        week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        self.time_containers = []
        self.day_containers = []

        dt = datetime.datetime.now()
        current_day =  dt.strftime("%A")

        for tableDay in week_days:
            if current_day.lower() == tableDay:
                for item in store.find(Day=tableDay):
                    self.day_containers.append(tableDay)
                    self.start_time = store.get(item[0])['Start_time']
                    self.time_containers.append(self.start_time)
        self.time_containers = self.time_containers
        self.day_containers = self.day_containers

        return self.time_containers,self.day_containers


#------------------------#######Validate alarm time########-----------------------------------#
    
    def validate_time(self,alarm_time):
        if len(alarm_time) != 11:
            return "Invalid time format! Please try again..."
        else:
            if int(alarm_time[0:2]) > 12:
                return "Invalid HOUR format! Please try again..."
            elif int(alarm_time[3:5]) > 59:
                return "Invalid MINUTE format! Please try again..."
            elif int(alarm_time[6:8]) > 59:
                return "Invalid SECOND format! Please try again..."
            else:
                return "ok"
    
#------------------------#######activating the control keys########-----------------------------------#
    # def get_thread_position(self,thread):
    #     import sys
    #     frame = sys._current_frames().get(thread.ident, None)
    #     if frame:
    #         return frame.f_code.co_filename, frame.f_code.co_name, frame.f_code.co_firstlineno


    paused = False 
    def on_press(self,key):
        global paused
        print (f"the key is: {key}")

        if key == "snooze": #snooze alarm
            Alarm.stream.stop_stream()
            time.sleep(5)

            #-----------this will open the popup box--------#
            summon_popup = Factory.pop_alarm()
            response = summon_popup.open()
            Alarm.stream.start_stream()
            paused = True
            return False

        elif key == "dismiss":
            curnt_threads = threading.active_count()

            if Alarm.stream.is_active(): 
                Alarm.stream.stop_stream()
                Alarm.stream.close()
                Alarm.p.terminate()
               
                caller = MainApp()
                # tmp = caller.pressed_button_alarm()
                caller2 = StoppableThread()
                try:
                    caller2.stop()
                    caller2.stopped()
                    print('i tried stopping the thread')
                    print('number of current threads is ', threading.active_count())

                except Exception as e:
                    print("i cannot stop the thread oooooo")
                    print('number of current threads is ', threading.active_count())

                    pass

                status = "i am alive , but will die now"
                print(status)
                paused = False
                    

        return paused

#------------------------#######converting starttime to desired 24hr format########-----------------------------------#
    
    def time_am_pm_rmval(self,time):
        if time[-2:].lower() == "am" and time[:2] == "12":
            # new_starttime = time[2:8]
            new_starttime =  "00:"+time[3:5]

        elif time[-2:].lower() == "am":
            # new_starttime = time[:-2]
            new_starttime = time[0:5]

        elif time[-2:].lower() == "pm" and time[:2] == "12":
            # new_starttime = time[:-2]
            new_starttime = time[0:5]

        else:
            new_starttime = str(int(time[:2]) + 12) + time[2:5]

        return new_starttime

#------------------------###############-----------------------------------#
    def time_difference(self , h1, m1, h2, m2):
	
        # convert current_time h1 : m1 into
        # minutes
        t1 = h1 * 60 + m1
        
        # convert alarm_time h2 : m2 into
        # minutes
        t2 = h2 * 60 + m2
        
        if (t1 == t2):
            value = "Both are same times"
            return value
        else:
            
            # calculating the difference
            diff = t2-t1
            
        # # calculating hours from
        # # difference
        # h = (int(diff / 60)) % 24
        
        # # calculating minutes from
        # # difference
        # m = (diff % 60)

        # # value1 = 'time difference is: {0}hr:{1}min'.format(h,m)
        # value2 = ((h*60) + m)


        return diff

#------------------------###############-----------------------------------#

    def alarm(self):
        
        print('number of current threads is ', threading.active_count())
        self.return_alarm_time()
        self.time_list = self.time_containers
        print(self.time_list )
        dt = datetime.datetime.now()
        curntime = dt.strftime("%H:%M")
        
        for tims in range(len(self.time_list)):
            # classtime = self.time_list[0]
            classtime = self.time_am_pm_rmval(self.time_list[0])

            curntim_hr =int(curntime[:2])
            curntim_min = int(curntime[3:5])
            alarm_hr = int(classtime[:2])
            alarm_min = int(classtime[3:5])
            # print(f"this is alarm hour: {alarm_hr} \n and this is alarm min {alarm_min}")
            difference = self.time_difference(curntim_hr,curntim_min,alarm_hr,alarm_min)
            # print(f"the difference is {difference}")
            if difference < 0 :
                response = "duration exceeded"
                self.time_list.pop(0)
                print(self.time_list)

            else:
               
                # if difference == 0:
                # try:
                time_day = self.day_containers[0]
                # print(f"i am the time list {self.time_list}")

                # you audio here
                wf = wave.open('./alarm_tones/alarm2.wav', 'rb')

                #-----------------------------------------------------------#
                # instantiate PyAudio
                p = pyaudio.PyAudio()
                    
                #-----------------------accepting alarm time and validate------------------------------------#
                alarm_time = self.time_list[0]
                print(alarm_time)
                
                alarm_time_2 = self.time_am_pm_rmval(alarm_time)
                # print("i am from am_pm removal {0}".format(alarm_time_2))
                validate_alarm = self.validate_time(alarm_time)

                if validate_alarm != "ok":
                    print("i am from validate time {0}".format(validate_alarm))

                else:
                    print(f"Setting alarm for {validate_alarm}...")
                    try:
                        print("scheduling task for day: {0} and time {1} ".format(time_day,alarm_time_2))
                        schedule.every().day.at(alarm_time_2).do(self.play_alarm_sound)
                        print("task scheduled already wait for response")   
                        while True:
                            schedule.run_pending()
                            time.sleep(1)
                            
                        
                    except Exception as e:
                        print(e)
                        # break
    
        
   
            
        # alarm_hour = int(alarm_time[0:2])
        # alarm_min = int(alarm_time[3:5])
        # alarm_sec = alarm_time[6:8]
        # alarm_period = alarm_time[9:].upper()

    def play_alarm_sound(self):
        
        #-----------this will open the popup box--------#
        summon_popup = Factory.pop_alarm()
        response = summon_popup.open()

        # define callback
        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return (data, pyaudio.paContinue)
        
        #-----------------------------------------------------------#
        # you audio here
        wf = wave.open('./alarm_tones/alarm2.wav', 'rb')

        #-----------------------------------------------------------#
        # instantiate PyAudio
        Alarm.p = pyaudio.PyAudio()

        #-----------------------------------------------------------#
        # open stream using callback
        Alarm.stream = Alarm.p.open(format=Alarm.p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        stream_callback=callback)
        
        Alarm.stream.start_stream()


        while Alarm.stream.is_active() ==True:
            print("Wake Up!")
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
            time.sleep(0.1)
        
        # stop stream
        Alarm.stream.stop_stream()
        Alarm.stream.close()
        wf.close()

        # close PyAudio
        Alarm.p.terminate()
# ----------------#----------------#-------------#------------#
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


#------------------------###############-----------------------------------#

#------------------------###############-----------------------------------#
class MainApp(MDApp):
    
    #------------------------------------------#
    # def Home_carousel_call():
    #     caller = Home_page()
    #     return caller.slide_images
   
    #-----------------------------------------------------------#
    def pressed_button_alarm(self):
        caller = Alarm()
        tmp = StoppableThread(target=caller.alarm)
        tmp.start()
        return tmp

    #------------------------------------------#
    def keyboard_listener_dismiss(self):
        caller = Alarm()
        caller.on_press("dismiss")
        
    #------------------------------------------#
    def keyboard_listener_snooze(self):
        caller = Alarm()
        caller.on_press("snooze")
   
    #-----------------------------------------------------------#
    def build(self):
        
        self.available_screens = sorted([
            'Home', 'Sign_up', 'verify', 'Login', 'UserMenu'
           ])
        self.screen_names = self.available_screens

    #------------------------------------------#
        self.screen_manager = ScreenManager()
    #-------------------------------------------#

    #-----------using the screen manager to refernce our Home page-------------#
        self.My_Home_page = Home_page()
        screen = Screen(name="Home")
        screen.add_widget(self.My_Home_page)
        self.screen_manager.add_widget(screen)

    # -----------using the screen manager to refernce our Sign_up page-------------#
        self.My_Sign_up_page = Sign_up_page()
        screen = Screen(name="Sign_up")
        screen.add_widget(self.My_Sign_up_page)
        self.screen_manager.add_widget(screen)

    #-----------using the screen manager to refernce our Sign_up page-------------#
        self.My_verify_page = verify_page()
        screen = Screen(name="verify")
        screen.add_widget(self.My_verify_page)
        self.screen_manager.add_widget(screen)

    #-----------using the screen manager to refernce our Login page-------------#
        self.My_Login_page = Login_page()
        screen = Screen(name="Login")
        screen.add_widget(self.My_Login_page)
        self.screen_manager.add_widget(screen)

    #-----------using the screen manager to refernce our Sign_up page-------------#
        self.My_UserMenu_page = UserMenu_page()
        screen = Screen(name="UserMenu")
        screen.add_widget(self.My_UserMenu_page)
        self.screen_manager.add_widget(screen)

    #-----------using the screen manager to refernce our Sign_up page-------------#
        # self.My_Calendar_page = Calendar_page()
        # screen = Screen(name="Calendar")
        # screen.add_widget(self.My_Calendar_page)
        # self.screen_manager.add_widget(screen)

    # #--------------using the screen manager to refernce our Sign_up page-------------#
        self.My_TTable_page = TimeTable_page()
        screen = Screen(name="TimeTable")
        screen.add_widget(self.My_TTable_page)
        self.screen_manager.add_widget(screen)
            
    #-----------using the screen manager to refernce our Assignment_page-------------#
        # self.My_scheduler_page = scheduler_page()
        # screen = Screen(name="Scheduler")
        # screen.add_widget(self.My_scheduler_page)
        # self.screen_manager.add_widget(screen)

    #-------------#-------------#------------#-----------#----------#   
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.set_colors("Blue", "600", "50", "800", "Teal", "600", "100", "800")

    #--------------#---------------#
        return self.screen_manager
    
    #------------------------###############-----------------------------------#
    # def kira_reminding2(self):
    #     caller = Alarm()
    #     kira()
    #     caller2 = UserMenu_page()
    #     caller3 = caller2.schedule_others_pop()
    #     print("after me then it's popupdata others")
    #     print(caller3.popupData_Others[0])

    #     dt = datetime.datetime.now()
    #     curntime = dt.strftime("%H:%M")

    #     kira.speak(f"""Hi, how are you ?,
    #         it's {curntime}  and  {caller2.popupData_Others[0]}""")

        
    #------------------------###############-----------------------------------#
    def kira_reminding(self):
        
        caller = Alarm()
        caller.return_alarm_time()

        # caller2 =  Home_page()
        # caller2.slide_images

        dt = datetime.datetime.now()

        
        time_list = caller.time_containers
        day_list = caller.day_containers
        # print(f"i am the time list1 {time_list}")
        new_time_list = []
      
        for i in time_list:
            i = caller.time_am_pm_rmval(i)
            i = dt.strptime(i, "%H:%M")
            new_time_list.append(i)
        # print(f"i am the time list2 b4 sort {new_time_list}")
        #-------------#-----sorting time list-----------#----------# 
        for i in range(len(new_time_list)-1):
            if new_time_list[i] < new_time_list[i+1]:
                new_time_list[i] = new_time_list[i]
                new_time_list[i] = new_time_list[i].strftime("%I:%M %p")
            else:
                new_time_list[i],new_time_list[i+1]  =  new_time_list[i+1],new_time_list[i]
                new_time_list[i] = new_time_list[i].strftime("%I:%M %p")
        new_time_list[-1] = new_time_list[-1].strftime("%I:%M %p")
        
        # print(f"i am the time list2 after sort {new_time_list}")
    #-------------#--------calculate difference frm currenttime-----#------------#-----------#----------#   
        curntime = dt.strftime("%H:%M")
        classtime = caller.time_am_pm_rmval(new_time_list[0])
        curntim_hr =int(curntime[:2])
        curntim_min = int(curntime[3:5])
        alarm_hr = int(classtime[:2])
        alarm_min = int(classtime[3:5])
        difference = caller.time_difference(curntim_hr,curntim_min,alarm_hr,alarm_min)

        print(f"this is the current differnce: {difference}")
        # print(f"this is the class time: {classtime}")
        kira_talk_time = dt.strptime(classtime, "%H:%M")
        kira_talk_time = kira_talk_time.strftime("%I:%M %p")
        # print(f"kira will say this: {kira_talk_time}")

        kira()
        # difference = abs(difference)
    #-------------#-------------#------------#-----------#----------#   
        if difference > 0 & difference <= 30:
            diff_hrs = (difference/60)
            print(f"difference in hours is: {diff_hrs}")

            kira.speak(f"""Hi, how are you ?,
            it's {curntime}  and you have a class scheduled for {kira_talk_time},
            that will be in next {difference} minutes,
            please do get ready so you will be able to meet up with your class,
            i'm counting on you,
            so make me proud ok ?""")
            # if difference > 5:
            #     # time.sleep((difference*60)- 3600)
            #     alarm_song = Alarm()
            #     t1 = threading.Thread(target=alarm_song.play_alarm_sound)
            #     # starting thread 1
            #     t1.start()
            #     try: 
            #         # wait until thread 1 is completely executed
            #         t1.join()
            #     except KeyboardInterrupt:
            #         # do nothing here
            #         pass

    #-------------#-------------#------------#-----------#----------#   
        elif difference <0 & difference >-5:
            kira.speak(f"""Hi, how are you ?
            it's {curntime} which is {difference} minutes past your scheduled time for your first class,
            hope you were able to make it to class early and didn't miss the class ?
            """)
            try:
                classtime = caller.time_am_pm_rmval(new_time_list[1])
                curntim_hr =int(curntime[:2])
                curntim_min = int(curntime[3:5])
                alarm_hr = int(classtime[:2])
                alarm_min = int(classtime[3:5])
                difference = caller.time_difference(curntim_hr,curntim_min,alarm_hr,alarm_min)
                kira_talk_time = dt.strptime(classtime, "%H:%M")
                kira_talk_time = kira_talk_time.strftime("%I:%M %p")

                kira.speak(f"""Also, i'll like to inform you about 
                    the upcoming class which start at {kira_talk_time},
                    that will be in next {difference} minutes as the time is {curntime}  now,
                    please do get ready so you will be able to meet up with your class,
                    i'm counting on you,
                    so make me proud ok ?""")
            except Exception:
                pass

    #-------------#-------------#------------#-----------#----------#   
        else:
            kira.speak(f"""Hi, how are you ?
            it's {curntime} which is {difference} minutes past your scheduled time for your class,
            hope you were able to make it to class early and didn't miss the class ?
            """)

            try:
                classtime = caller.time_am_pm_rmval(new_time_list[1])
                # for i in range(len(time_list)):
                curntim_hr =int(curntime[:2])
                curntim_min = int(curntime[3:5])
                alarm_hr = int(classtime[:2])
                alarm_min = int(classtime[3:5])
                difference = caller.time_difference(curntim_hr,curntim_min,alarm_hr,alarm_min)
                kira_talk_time = dt.strptime(classtime, "%H:%M")
                kira_talk_time = kira_talk_time.strftime("%I:%M %p")

                kira.speak(f"""Also, i'll like to inform you about 
                    the upcoming class which start at {kira_talk_time},
                    that will be in next {difference} minutes as the time is {curntime}  now,
                    please do get ready so you will be able to meet up with your class,
                    i'm counting on you,
                    so make me proud ok ?""")
            except Exception:
                pass
        
    #------------------------###############-----------------------------------#
    
if __name__ == '__main__':
    reminder_app = MainApp()
    t1 = threading.Thread(target=reminder_app.kira_reminding)
    # t2 = threading.Thread(target=reminder_app.kira_reminding2)
    
    # starting thread 1
    # timer = threading.Timer(2.0, t1.start)
    # timer.start()
    t1.start()
        
    # t2.start()
    # starting reminder app 
    reminder_app.run()

    
    # wait until thread 1 is completely executed
    # t1.join()
    # t2.start()
    # t2.join()
    
    
  


