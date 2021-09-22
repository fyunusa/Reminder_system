from kivy.app import App
from kivymd.app import MDApp
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
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.factory import Factory
#----------------#----------------#-------------#------------#
import datetime
import pprint
#----------------#----------------#-------------#------------#
Builder.load_file("lab3.kv")
# Builder.load_file("popup.kv")

#----------------#----------------#-------------#------------#
store = JsonStore('user_data.json')
#-----------------------------------------------------------#
#-----------------------------------------------------------#
class UserMenu_page(Screen):

    def pressed_button_home(self, instance):
        reminder_app.screen_manager.current = "Home"
#-----------------------------------------------------------#
    def pressed_button_const(self, instance):
        reminder_app.screen_manager.current = "UserMenu"
#-----------------------------------------------------------#
    def pressed_button_scheduler(self, instance):
        reminder_app.screen_manager.current = "Scheduler"
#-----------------------------------------------------------#
    def pressed_button_calender(self, instance):
        reminder_app.screen_manager.current = "Calendar"
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
    def schedule_pop(self):
        summon_popup = Factory.pop()
        response = summon_popup.open()
        dt = datetime.datetime.now()
        popupData = []
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

            #----------------#----------------#-------------#------------#
                    if start_time[-2:] == "am" and start_time[:2] == "12":
                        print ("00" + start_time[2:-2])
                        new_starttime = "00" + start_time[2:-2]

                    elif start_time[-2:] == "am":
                        print (start_time[:-2])
                        new_starttime = start_time[:-2]

                    elif start_time[-2:] == "pm" and start_time[:2] == "12":
                        print (start_time[:-2])
                        new_starttime = start_time[:-2]

                    else:
                        print (str(int(start_time[:2]) + 12) + start_time[2:5])
                        new_starttime = str(int(start_time[:2]) + 12) + start_time[2:5]

            #----------------#----------------#-------------#------------#
                    processedData = "Upcoming {0} classes {1} which starts at {2} and ends at {3}".format(current_day, course_code, start_time, end_time )
                    popupData.append(processedData)

            #----------------#----------------#-------------#------------#
                    fmt = "%H:%M"
                    time_diff = dt.strptime(new_starttime, fmt) - dt.strptime(current_time_hr, fmt)
                    print("i am time different",time_diff)
                    

            #----------------#----------------#-------------#------------#
                    total_seconds = time_diff.total_seconds()
                    total_minutes = int(total_seconds/60)
                    total_hours = int(total_minutes/60)
                    total_days = int(total_hours/24)
                    print(total_minutes, total_hours, total_days)

            #----------------#----------------#-------------#------------#
                    if total_minutes <= 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)
                        print(response_text)
                    
                    elif total_minutes > 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)
                        print(total_minutes)
                        print(response_text)

                    elif total_minutes < 0 and total_minutes < -1:
                        response_text = "From my little knowledge i can see that {0} is past {1} minutes already, is it safe to assume that you did not miss your class".format(course_code, total_minutes)
                        print(response_text)        

            #----------------#----------------#-------------#------------#
            popupData_convert = ','.join(popupData)   
            summon_popup.ids.popuptext.text = popupData_convert
            headText = "{0} Upcoming Scheduled Classes".format(current_day)
            summon_popup.title = headText

    pass

#------------------------###############-----------------------------------#
#Working with main App
#------------------------###############-----------------------------------#
class MainApp(MDApp):

    def build(self):
        self.screen_manager = ScreenManager()
        # Clock.schedule_interval(my_Popup, 0.5)
    #-----------using the screen manager to refernce our Sign_up page-------------#
        self.My_UserMenu_page = UserMenu_page()
        screen = Screen(name="UserMenu")
        screen.add_widget(self.My_UserMenu_page)
        self.screen_manager.add_widget(screen)
    

        return self.screen_manager
    
    
        
if __name__ == '__main__':
    reminder_app = MainApp()
    reminder_app.run()

