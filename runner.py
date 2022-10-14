from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="листай дальше")
        btn.on_press = self.next
        self.add_widget(btn) # экран - это виджет, на котором могут создаваться все другие (потомки)
        
    def next(self):
        self.manager.transition.direction = 'left' # объект класса Screen имеет свойство manager 
   # - это ссылка на родителя
        self.manager.current = 'second'
    
    
class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="листай дальше")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'thirt'#переключения экранов 


class ThScr(Screen):
    def __init__(self, name='thirt'):
        super().__init__(name=name)
        btn = Button(text="листай листай")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'four'#переключения экранов 

class FrScr(Screen):
    def __init__(self, name='four'):
        super().__init__(name=name)
        btn = Button(text="еще чучуть")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'five'#переключения экранов 

class FvScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        btn = Button(text="спорим ты ничего не делал")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        next
        
       

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThScr())
        sm.add_widget(FrScr())
        sm.add_widget(FvScr())

        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm
    

app = MyApp()
app.run()