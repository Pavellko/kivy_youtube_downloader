# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image

from pytube import YouTube
import os

Window.clearcolor = '#d62926'

class Scr1(Screen):
   ''' Тут виджеты первого экрана'''
   def __init__(self, **kwargs):
      super().__init__(**kwargs)

      img1 = Image(source="puls2.jpg")

      pulse1 = Label(text="Скачаем музычку!", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5}, font_size = '30dp' )
            
      imya1 = Label(text='Закидывай сюда ссылочку на Ютюб', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
      self.in_name = TextInput(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5}, multiline=False)


      self.btn = Button(text='Погнали!', pos_hint={'center_x': 0.5},  size_hint=(0.5, 0.2))
      self.btn.background_color = (1,0,0,1)
      line1 = BoxLayout(orientation='vertical', padding=50)

      line1.add_widget(img1)
      line1.add_widget(pulse1)

      line1.add_widget(imya1)
      line1.add_widget(self.in_name)


      line1.add_widget(self.btn)

      self.add_widget(line1)
      self.btn.on_press = self.next

   def next(self):
      global link
      link = self.in_name.text
      self.manager.current = 'scr2'


class Scr2(Screen):
   ''' Тут виджеты 3-го экрана'''
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.img2 = Image()
      self.img2.source = 'not-bad.jpg'
      self.outer = BoxLayout(orientation='vertical', padding=50, spacing=8)
      self.instr = Label(text = '', font_size = '30dp')
      self.instr.text = 'Файлик скачивается!'
      self.btn3 = Button(text='Ещё разок?', pos_hint={'center_x': 0.5},  size_hint=(0.3, 0.1))
      self.btn3.background_color = (1,0,0,1)

      self.btn3.on_press = self.nazad
      self.outer.add_widget(self.img2)
      self.outer.add_widget(self.instr)
      self.outer.add_widget(self.btn3)
      self.add_widget(self.outer)
      self.on_enter = self.before
  
   def before(self):
      global link
      print(link)
      yt = YouTube(str(link))
      videos = yt.streams.get_audio_only()
      videos.download()


   def nazad(self):
      self.manager.current = 'scr1'


 
class Windows10(App):
   ''' Тут создаются экраны '''
   def build(self):
      sm = ScreenManager()
      sm.add_widget(Scr1(name='scr1'))
      sm.add_widget(Scr2(name='scr2'))

      return sm
 
app = Windows10()
app.run()