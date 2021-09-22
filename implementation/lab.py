from kivy.lang import Builder
from kivymd.app import MDApp


class MyApp(MDApp):
    def build(self):
    return Builder.load_string(KV)
    MyApp().run()
