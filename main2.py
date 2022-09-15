from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from pytube import YouTube

class MyApp(App):

    def build(self):
        lb = Label(text='Это мой ютюб доунлодер!')
        self.link = TextInput(focus = True)
        btn = Button(text='Скачать', )
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(lb)
        box.add_widget(self.link)
        box.add_widget(btn)
        btn.on_press = self.next
        return box
    
    def next(self):
        link = self.link.text

        yt = YouTube(link)
        videos = yt.streams.get_audio_only()
        videos.download()

app = MyApp()
app.run()