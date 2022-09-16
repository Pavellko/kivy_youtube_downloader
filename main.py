from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from pytube import YouTube

Window.clearcolor = (0.24, 0.38, 0.66, 1)
link = ''
class Scr1(Screen):
    def __init__(self, **x):
        super().__init__(**x)
        self.img = Image( source="puls2.jpg" )

        self.lb = Label(text='Это наш скачивальщик!', font_size = '30dp')
        self.link = TextInput( size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5} )

        self.btn = Button(text='Скачать')
        line1 = BoxLayout(orientation='vertical', padding=50)

        line1.add_widget(self.img)
        
        line1.add_widget(self.lb)
        line1.add_widget(self.link)
        line1.add_widget(self.btn)

        self.btn.on_press = self.gosecond
        self.add_widget(line1)
    def gosecond(self):
        global link
        link = self.link.text
        self.manager.current = 'scr2'

class Scr2(Screen):
    def __init__(self, **x):
        super().__init__(**x)
        self.btn2 = Button(text='Назад', pos_hint={'center_x': 0.5, 'center_y': 0.2},  size_hint=(0.3, 0.2))
        self.add_widget(self.btn2)

        self.on_enter = self.funk2
        self.btn2.on_press = self.gofirst
    def gofirst(self):
        self.manager.current = 'scr1'
    def funk2(self):
        global link
        
        YouTube(str(link)).streams.get_audio_only().download()


    



class Windows10(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget( Scr1(name='scr1') )
        sm.add_widget( Scr2(name='scr2') )
        return sm

app = Windows10()
app.run()



