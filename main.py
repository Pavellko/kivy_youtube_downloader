from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from pytube import YouTube

Window.clearcolor = '#d62926'

class Scr1(Screen):
    def __init__(self, **x):
        super().__init__(**x)
        self.lb = Label(text='Это наш скачивальщик!')
        self.btn = Button(text='Скачать')
        line1 = BoxLayout(orientation='vertical', padding=50)

        line1.add_widget(self.lb)
        line1.add_widget(self.btn)

        self.btn.on_press = self.gosecond
        self.add_widget(line1)
    def gosecond(self):
        self.manager.current = 'scr2'

class Scr2(Screen):
    def __init__(self, **x):
        super().__init__(**x)
        self.btn2 = Button(text='Назад')
        self.btn2.on_press = self.gofirst
    def gofirst(self):
        self.manager.current = 'scr2'


class Windows10(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget( Scr1(name='scr1') )
        sm.add_widget( Scr2(name='scr2') )
        return sm

app = Windows10()
app.run()



