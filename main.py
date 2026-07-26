from kivy.app import App
from kivy.uix.button import Button

class DukanHisaabApp(App):
    def build(self):
        return Button(text='Dukan Hisaab App - Hello!')

if __name__ == '__main__':
    DukanHisaabApp().run()
  
