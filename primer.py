from kivy.app import App

from kivy.uix.button  import Button
from kivy.uix.label  import Label
from kivy.uix.boxlayout  import BoxLayout

class MyApp(App):

    def build(self):
        lb = Label(text="Это надпись")

        btn = Button(text='Это кнопка')
        box = BoxLayout(orientation ='vertical',padding=8, spacing=8)

        box.add_widget(lb)
        box.add_widget(btn)

        btn.on_press = self.funk
        return box

    def funk(self):
        print("нажатие")

app = MyApp()
app.run()
