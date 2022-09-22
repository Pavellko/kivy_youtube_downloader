from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from pytube import YouTube
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (1 , 0 , 0 , 1)

class MyApp(App):

    def build(self):
        lb = Label(text='Это мой ютюб доунлодер!', font_size = '30dp' )
        img = Image(source="puls2.jpg")
        self.link = TextInput( size_hint=(0.5, 0.2), pos_hint = {'center_x': 0.5}  )

        btn = Button(text='Скачать', pos_hint={'center_x': 0.5},   size_hint=(0.5, 0.2) )
        btn2 = Button(text='Проиграть', pos_hint={'center_x': 0.5},   size_hint=(0.5, 0.2) )
        
        box = BoxLayout(orientation = 'vertical', padding=50)
        box.add_widget(img)
        box.add_widget(lb)
        box.add_widget(self.link)
        box.add_widget(btn)
        box.add_widget(btn2)
        btn.on_press = self.next
        btn2.on_press = self.play
        return box
    
    def next(self):
        YouTube(self.link.text).streams.get_audio_only().download()

    def play(self):
        import glob, os
        file_name = glob.glob('*.mp4')[0]
        os.startfile(file_name)

app = MyApp()
app.run()