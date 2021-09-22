import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
import re
from kivy.storage.jsonstore import JsonStore
store = JsonStore('user_data.json')




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
        containertime = []
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
                    popupData.append(processedData)
                    containertime.append(new_starttime)

                    fmt = "%H:%M"
                    time_diff = dt.strptime(new_starttime, fmt) - dt.strptime(current_time_hr, fmt)

                    total_seconds = time_diff.total_seconds()
                    total_minutes = int(total_seconds/60)

            #----------------#-----------using total minutes to decide next class-----#-------------#------------#
                    if total_minutes <= 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)
                    
                    elif total_minutes > 120 and total_minutes >= 0:
                        response_text = "{0} {1} is coming up in next {2} minutes by {3}".format(course_code, course_title, total_minutes,start_time)

                    elif total_minutes < 0 and total_minutes < -1:
                        response_text = "From my little knowledge i can see that {0} is past {1} minutes already, is it safe to assume that you did not miss your class ?".format(course_code, total_minutes)
                    
                    self.ids.user_menu_widget3.text = response_text

            #----------------#-------sort time container--------#-------------#------------#
                    sorter = containertime.sort()
                    print(containertime)
                    try:
                        j = 0
                        for i in containertime:
                            print(i)
                    #         if containertime[j] > containertime[ j + 1]:
                    #             first_ele = containertime.pop(containertime[j])
                    #             second_ele = containertime.pop(containertime[j + 1])
                    #             containertime.insert(j,second_ele)
                    #             containertime.insert(j + 1, first_ele)
                    #             for item in store.find(course_StartTime=containertime[j]):
                    #                 first_result = item[0]
                    #                 print(first_result)
                    #         else:
                    #             for item in store.find(course_StartTime=containertime[j]):
                    #                 first_result = item[0]
                    #                 print(first_result)

                    #     j = j + 1
                    #     print("reviewed container",containertime)
                    except Exception as e:
                        print('exception error occured as: ',e)
            # print('{0} is greater than {1}'.format(containertime[j],containertime[j + 1]))
        
            #----------------#----------------#-------------#------------#
            popupData_convert = ','.join(popupData)   
            summon_popup.ids.popuptext.text = popupData_convert
            
            headText = "{0} Upcoming Scheduled Classes".format(current_day)
            summon_popup.title = headText
    # #----------------#-------sort time container---------#-------------#------------#
    #     sorter = containertime.sort()
    #     try:
    #         j = 0
    #         for i in containertime:
    #             if containertime[j] > containertime[ j + 1]:
    #                 first_ele = containertime.pop(containertime[j])
    #                 second_ele = containertime.pop(containertime[j + 1])
    #                 containertime.insert(j,second_ele)
    #                 containertime.insert(j + 1, first_ele)
    #         j = j + 1
    #         print("reviewed container",containertime)
    #     except Exception as e:
    #         print(e)
    #         # print('{0} is greater than {1}'.format(containertime[j],containertime[j + 1]))
        
    #----------------#----------------#-------------#------------#
    
#-----------------------------------------------------------#
    pass
#-----------------------------------------------------------#

class MyApp(MDApp):
    #         self.username = TextInput(text=previous_username,multiline=False) # Create a Text input box stored in the name variable

#-----------------------------------------------------------#
    def build(self):
        #-----------using the screen manager to refernce our Sign_up page-------------#
        self.My_UserMenu_page = UserMenu_page()
        screen = Screen(name="UserMenu")
        screen.add_widget(self.My_UserMenu_page)
        self.screen_manager.add_widget(screen)
#-----------------------------------------------------------#   
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
#-----------------------------------------------------------#
        # return Builder.load_file("scheduler.kv")
#-----------------------------------------------------------#

  return self.screen_manager
        
if __name__ == '__main__':
    reminder_app = MainApp()
    reminder_app.run()