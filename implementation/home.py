from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextFieldRound
#----------------#----------------#-------------#------------#
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
#----------------#----------------#-------------#------------#
from kivy.uix.label import Label
from kivy.uix.widget import Widget
#----------------#----------------#-------------#------------#
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.picker import MDDatePicker, MDTimePicker
#----------------#----------------#-------------#------------#
import os
import datetime
import time
import re
#----------------#----------------#-------------#------------#
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.factory import Factory


#----------------#---------Voice-------#-------------#------------#
# import speech_recognition as sr  
import speech_recognition as s_r


#----------------#------------json's----#-------------#------------#
store = JsonStore('user_data.json')

#----------------#---------Kv's-------#-------------#------------#
Builder.load_file("home.kv")
Builder.load_file("new_login.kv")
Builder.load_file("sign_up.kv")
Builder.load_file("calendar.kv")
Builder.load_file("Ttable.kv")
Builder.load_file("assignment.kv")
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

    def pressed_button_SignUp(self, instance):
        reminder_app.screen_manager.current = "Sign_up"
    
    def pressed_button_Verify(self, instance):
        reminder_app.screen_manager.current = "Sign_up2"

    def pressed_button_UMenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
    
    def talk_kira(self):
        r = s_r.Recognizer()
        my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
        with my_mic as source:
            print("Say now!!!!")
            r.adjust_for_ambient_noise(source) #reduce noise
            audio = r.listen(source) #take voice input from the microphone
        print(r.recognize_google(audio)) #to print voice into text

    
    def slide_images(self, *args):

        #----------------#------slider parameters------------#------------#
        
        images_list = ['./images/convert1.jpg','./images/convert2.jpg','./images/convert3.jpg','./images/convert4.jpg','./images/convert5.jpg','./images/convert6.jpg']
        images_text_list = ['we do not forgive', 'we do not forget', 'we are unstoppable']
        
        read_quote_file = open('./inspirational_quotes.txt', 'r')
        read_advantage_file = open('./advan.txt', 'r')
        quotes = read_quote_file.readlines()
        advantages = read_advantage_file.readlines()

        self.ids.slide_img.min = 0
        self.ids.slide_img.max = len(images_list)
        self.ids.slide_img.step = 1

        # self.ids.image_tite.source = images_list[0]
        for i in range(len(images_list)):
            if self.ids.slide_img.value  == i:
                self.ids.image_tite.source = images_list[i]
                self.ids.image_tite.text = quotes[i]


        for i in range(len(quotes)):
            if i%2 == 1:
                i = i + 1
            elif i%2 != 1: 
                i = i
            if self.ids.slide_img.value  == i:
                if i < len(quotes):
                    quote_length = len(quotes[i])
                    if quote_length <= 80:
                        self.ids.quote_widget.text = quotes[i]+quotes[i+1]
                    else:
                        self.ids.quote_widget.text = quotes[i][0:80]+'\n'+quotes[i][80:quote_length]+'\n'+quotes[i+1]
        
            
        for i in range(len(advantages)):
            if self.ids.slide_img.value  == i:
                if i < len(advantages):
                    advantage_length = len(advantages[i])
                    if advantage_length <= 80:
                        self.ids.advantage_widget.text = advantages[i]
                    else:
                        self.ids.advantage_widget.text = advantages[i][0:80]+'\n'+advantages[i][80:advantage_length]

                
        
        # print(quotes)

    pass
#-----------------------------------------------------------#

class Login_page(Screen):

    def pressed_button_back(self, instance):
        reminder_app.screen_manager.current = "Home"
    
    def pressed_button_SignUp(self, instance):
        reminder_app.screen_manager.current = "Sign_up"
    
    def pressed_button_Verify(self, instance):
        reminder_app.screen_manager.current = "Sign_up2"

    def login_logger(self):
        self.root.ids.welcome_label.text = f'welcome {self.root.ids.user.text } !'
        
        with open("previous_details.txt", "w") as f:
            f.write(f"{self.root.ids.user.text},{self.root.ids.password.text }")

    def login_clear(self):

        self.root.ids.welcome_label.text = "welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    pass

#-----------------------------------------------------------#
class UserMenu_page(Screen):

    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
    
        if store.exists('exam_date'):
            report = store.get('exam_date')['days_left'] 
            self.ids.user_menu_widget2.text = str(report) + "\nDays"
            print(report)
        
        else:
            print("Exam date not available")
        
#-----------------------------------------------------------#
    def pressed_button_scheduler(self, instance):
        reminder_app.screen_manager.current = "Scheduler"
#-----------------------------------------------------------#
    def pressed_button_calender(self, instance):
        reminder_app.screen_manager.current = "Calendar"
#-----------------------------------------------------------#
    def pressed_button_assignments(self, instance):
        reminder_app.screen_manager.current = "Assignment"
#-----------------------------------------------------------#
    def pressed_button_record(self, instance):
        reminder_app.screen_manager.current = "Record"
#-----------------------------------------------------------#
    def pressed_button_timetable(self, instance):
        reminder_app.screen_manager.current = "TimeTable"
#-----------------------------------------------------------#
    def pressed_button_pop(self, instance):
        reminder_app.screen_manager.current = "MyPopup"
#-----------------------------------------------------------#
    def slide_it(self, *args):

        scheduler = self.schedule_pop()
        #----------------#------slider parameters------------#------------#
        self.ids.slide_class1.min = 0
        self.ids.slide_class1.max = len(self.popupData)
        self.ids.slide_class1.step = 1

        for i in range(len(self.popupData)) :
            if self.ids.slide_class1.value  == i:
                self.slide_text.text = self.popupData[i]
                
        print(self.popupData)

#-----------------------------------------------------------#
    def schedule_pop(self):
        summon_popup = Factory.pop()
        #-----------this will open the popup box--------#
        # response = summon_popup.open()
        dt = datetime.datetime.now()
        self.popupData = []
        self.containertime = []
        row_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
    #----------------#----------------#-------------#------------#
        current_day =  dt.strftime("%A")
        current_time = dt.strftime('%I:%M %p')
        current_time_hr = dt.strftime("%H:%M")
    
    #----------------#----------------#-------------#------------#
        for tableDay in row_days:
            if current_day.lower() == tableDay:
                for item in store.find(day=tableDay):
                    course_code = store.get(item[0])['code']
                    course_title = store.get(item[0])['title']
                    start_time = store.get(item[0])['course_StartTime']
                    end_time = store.get(item[0])['course_EndTime']

            #----------------#--------converting starttime to desired format--------#-------------#------------#
                    if start_time[-2:] == "am" and start_time[:2] == "12":
                        new_starttime = "00" + start_time[2:-2]

                    elif start_time[-2:] == "am":
                        new_starttime = start_time[:-2]

                    elif start_time[-2:] == "pm" and start_time[:2] == "12":
                        new_starttime = start_time[:-2]

                    else:
                        new_starttime = str(int(start_time[:2]) + 12) + start_time[2:5]

            #----------------#----------------#-------------#------------#
                    processedData = "Upcoming {0} classes {1} which starts at {2} and ends at {3}".format(current_day, course_code, start_time, end_time)

            #----------------#------populate containers----------#-------------#------------#
                    self.popupData.append(processedData)
                    self.containertime.append(new_starttime)

                    fmt = "%H:%M"
                    time_diff = dt.strptime(new_starttime, fmt) - dt.strptime(current_time_hr, fmt)

                    total_seconds = time_diff.total_seconds()
                    total_minutes = int(total_seconds/60)

            #----------------#-----------using total minutes to decide next class at widget3-----#-------------#------------#
                    if total_minutes <= 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)
                    
                    elif total_minutes > 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)

                    elif total_minutes < 0 and total_minutes < -1:
                        response_text = "From my little knowledge i can see that {0} is past {1} minutes already, is it safe to assume that you did not miss your class ?".format(course_code, total_minutes)
                    
                    # self.ids.user_menu_widget3.text = response_text

            #----------------#----------------#-------------#------------#
            popupData_convert = ','.join(self.popupData)   
            summon_popup.ids.popuptext.text = popupData_convert

            #----------------#------popup title text------------#------------#
            headText = "{0} Upcoming Scheduled Classes".format(current_day)
            summon_popup.title = headText

        # return containertime

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
    def pressed_button_SignUp2(self, instance):
        reminder_app.screen_manager.current = "Sign_up2"
#-----------------------------------------------------------#
    def pressed_button_submit(self):
#-----------------------------------------------------------#
        self.users_Fname = self.ids.F_name.text
        users_Sname = self.ids.S_name.text
        users_School = self.ids.School.text
        users_Email =  self.ids.Email.text
        users_Faculty = self.ids.Faculty.text
        users_Department = self.ids.Department.text
        
#-----------------------------------------------------------#

        store.put(
            self.users_Fname, 
            name = self.users_Fname,
            surname = users_Sname,
            school = users_School,
            email = users_Email,
            faculty = users_Faculty,
            department = users_Department
            )

        reminder_app.screen_manager.current = "Sign_up2"

    pass
#-----------------------------------------------------------#

class Sign_up_page2(Screen):

#-----------------------------------------------------------#

    def pressed_button_login(self, instance):
        reminder_app.screen_manager.current = "Login"
#-----------------------------------------------------------#

    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Sign_up2"
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

            reminder_app.screen_manager.current = "Sign_up2"

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

                reminder_app.screen_manager.current = "Sign_up2"  
            print(text)
#-----------------------------------------------------------#
    pass
#-----------------------------------------------------------#

class Calendar_page(Screen):

    try:

        def show_date_picker(self):
            '''Open date picker dialog.'''
            date_dialog = MDDatePicker()
            date_dialog.bind(date=self.get_date)
            date_dialog.open()
    #-----------------------------------------------------------#
        def show_time_picker(self):
            '''Open time picker dialog.'''
            time_dialog = MDTimePicker()
            time_dialog.bind(time=self.get_time)
            time_dialog.open()
    #-----------------------------------------------------------#
        def get_time(self, instance, time):
            '''The method returns the set time.'''
            self.received_time = time
            print(self.received_time)
    #-----------------------------------------------------------#
        def on_save(self, instance, value, date_range):
            '''
                Events called when the "OK" dialog box button is clicked.
                :type instance: <kivymd.uix.picker.MDDatePicker object>;
                :param value: selected date;
                :type value: <class 'datetime.date'>;
                :param date_range: list of 'datetime.date' objects in the selected range;
                :type date_range: <class 'list'>;
            '''
            dt = datetime.datetime.now()
        
            current_Date1 = dt.strftime('%Y,%m,%d')
            received_Date1 = value.strftime('%Y,%m,%d')

            current_Date2 = datetime.datetime.strptime(current_Date1,'%Y,%m,%d')
            received_Date2 = datetime.datetime.strptime(received_Date1 ,'%Y,%m,%d')

            days_difference = (received_Date2 - current_Date2).days
            
            # print(days_difference)
            # self.report = "total days left is: {0} ".format(days_difference)
            store.put('exam_date', days_left = days_difference)
            # print(self.report)

        def on_cancel(self, instance, value):
            '''Events called when the "CANCEL" dialog box button is clicked.'''
    #-----------------------------------------------------------#
        def show_date_picker(self):
            date_dialog = MDDatePicker()
            date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
            date_dialog.open()
    
    except Exception:
        pass

#-----------------------------------------------------------#
    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Calendar"
#-----------------------------------------------------------#
    def pressed_button_record(self, instance):
        reminder_app.screen_manager.current = "TimeTable"
#-----------------------------------------------------------#
    def pressed_button_assignments(self, instance):
        reminder_app.screen_manager.current = "Assignment"
#-----------------------------------------------------------#
    def pressed_button_usermenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    pass
#-----------------------------------------------------------#

class TimeTable_page(Screen):
#-----------------------------------------------------------#
#-----------------------------------------------------------#
    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
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
            for item in store.find(day=days):
                json_data_collector = (
                    # The number of elements must match the length
                    # of the `column_data` list.
                    
                        count,
                        ( "alert-circle", [255 / 256, 165 / 256, 0, 1], store.get(item[0])['day']),# for a row with icon
                        store.get(item[0])['course_StartTime'],
                        store.get(item[0])['course_EndTime'],
                        store.get(item[0])['code'],
                        store.get(item[0])['title'],
                        store.get(item[0])['unit'],
                    )
                
                user_row_data.append(json_data_collector)
                count += 1
            # print(user_row_data)

        # operate1 = ''.join(str(e) for e in user_row_data)
        # print("\n" + str(operate1))

        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint = {'center_y': 0.5, 'center_x': 0.5},
            use_pagination = True,

            column_data=[
                ("No.", dp(15)),
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
        self.add_widget(self.data_tables)
        return self.TTable_layout



    def sort_on_col_units(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][3]
            )
        )

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
    
    def sort_on_title(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-2]))

    def sort_on_day(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-6]))

    
    def clicker_button(self):
        self.pressed_button_timetable()
#-----------------------------------------------------------#

    pass
#-----------------------------------------------------------#
class Assignment_page(Screen):
    #-----------------------------------------------------------#
    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Assignment"
#-----------------------------------------------------------#
    def pressed_button_calendar(self, instance):
        reminder_app.screen_manager.current = "Calendar"
#-----------------------------------------------------------#
    def pressed_button_usermenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def pressed_button_timetable(self, instance):
        reminder_app.screen_manager.current = "TimeTable"
#-----------------------------------------------------------#
    def pressed_button_assignment(self, *args):
        self.ATable_layout = AnchorLayout()

        user_row_data=[]
        row_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        count = 1

        for days in row_days:
            if store.exists('Assignments'):
                json_data_collector = (
                    # The number of elements must match the length
                    # of the `column_data` list.
                    
                        count,
                    ( 
                        store.get('Assignments')['Course_Title'],
                        store.get('Assignments')['Question'],
                        store.get('Assignments')['Due_date'],
                    )
                )
                
                user_row_data.append(json_data_collector)
                count += 1

        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint = {'center_y': 0.5, 'center_x': 0.5},
            use_pagination = True,

            column_data=[
                ("No.", dp(10)),
                ("[color=#52251B] Course Title [/color]", dp(45)),
                ("[size=15] Question [/size]", dp(60)),
                ("Due Date", dp(15),),
            ],

            row_data = user_row_data,
            elevation = 20,

        )
        self.add_widget(self.data_tables)
        return self.ATable_layout

    def clicker_button(self):
        self.pressed_button_assignment()
    
    pass
#-----------------------------------------------------------#
class scheduler_page(Screen):

    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "Scheduler"
#-----------------------------------------------------------#
    def pressed_button_assignment(self, instance):
        reminder_app.screen_manager.current = "Assignment"
#-----------------------------------------------------------#
    def pressed_button_timetable(self, instance):
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
                    if quote_length <= 20:
                        self.ids.quote_widget.text = quotes[i]+quotes[i+1]
                    else:
                        self.ids.quote_widget.text = quotes[i][0:20]+'\n'+quotes[i][20:40]+'\n'+quotes[i][40:60]+'\n'+quotes[i+1]
        
#-----------------------------------------------------------#

    def pressed_button_usermenu(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def class_scheduler(self):
        ids = ['Day','Start_time', 'End_time','course_code','course_title','credit_unit']
        hint_texts = ['Day e.g monday','Start Time e.g 07:00','End Time e.g 04:00','course_code','Course Title ','credit_unit']

        try:
            for i in range(len(ids)):
                inputs = MDTextFieldRound(
                    id = ids[i],
                    icon_left = "account",
                    hint_text = hint_texts[i],
                    width = 500,
                    font_size = 18,
                    )
                
                self.ids.schedule_something.add_widget(inputs)
        except Exception as e:
            print(e)
            
         
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
#-----------------------------------------------------------#
    pass

#------------------------###############-----------------------------------#
class MainApp(MDApp):

    def build(self):
        self.screen_manager = ScreenManager()
        # Clock.schedule_interval(slide_it(), 0.5)

     #-----------using the screen manager to refernce our Home page-------------#
        self.My_Home_page = Home_page()
        screen = Screen(name="Home")
        screen.add_widget(self.My_Home_page)
        self.screen_manager.add_widget(screen)

    # #-----------using the screen manager to refernce our Sign_up page-------------#
    #     self.My_Sign_up_page = Sign_up_page()
    #     screen = Screen(name="Sign_up")
    #     screen.add_widget(self.My_Sign_up_page)
    #     self.screen_manager.add_widget(screen)

    # #-----------using the screen manager to refernce our Sign_up page-------------#
    #     self.My_Sign_up_page2 = Sign_up_page2()
    #     screen = Screen(name="Sign_up2")
    #     screen.add_widget(self.My_Sign_up_page2)
    #     self.screen_manager.add_widget(screen)

    # #-----------using the screen manager to refernce our Login page-------------#
    #     self.My_Login_page = Login_page()
    #     screen = Screen(name="Login")
    #     screen.add_widget(self.My_Login_page)
    #     self.screen_manager.add_widget(screen)

    # #-----------using the screen manager to refernce our Sign_up page-------------#
#         self.My_UserMenu_page = UserMenu_page()
#         screen = Screen(name="UserMenu")
#         screen.add_widget(self.My_UserMenu_page)
#         self.screen_manager.add_widget(screen)

#     # #-----------using the screen manager to refernce our Sign_up page-------------#
#         self.My_Calendar_page = Calendar_page()
#         screen = Screen(name="Calendar")
#         screen.add_widget(self.My_Calendar_page)
#         self.screen_manager.add_widget(screen)

#     #--------------using the screen manager to refernce our Sign_up page-------------#
#         self.My_TTable_page = TimeTable_page()
#         screen = Screen(name="TimeTable")
#         screen.add_widget(self.My_TTable_page)
#         self.screen_manager.add_widget(screen)

# #-----------using the screen manager to refernce our Assignment_page-------------#
#         self.My_Assignment_page = Assignment_page()
#         screen = Screen(name="Assignment")
#         screen.add_widget(self.My_Assignment_page)
#         self.screen_manager.add_widget(screen)
#         scheduler_page
    
# #-----------using the screen manager to refernce our Assignment_page-------------#
        self.My_scheduler_page = scheduler_page()
        screen = Screen(name="Scheduler")
        screen.add_widget(self.My_scheduler_page)
        self.screen_manager.add_widget(screen)

#-------------#-------------#------------#-----------#----------#   
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.set_colors("Blue", "600", "50", "800", "Teal", "600", "100", "800")
    
    #--------------#---------------#
        return self.screen_manager
    
if __name__ == '__main__':
    reminder_app = MainApp()
    reminder_app.run()



