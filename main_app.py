from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation

class AnimatedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        start_color = self.background_color
        start_size_h = self.size_hint
        start_pos_hint = self.pos_hint
        start_font_size = self.font_size

        animate = Animation(background_color=(0, 0, 1, 1), duration=1.5)
        animate = animate + Animation(size_hint=(1, 1))
        animate = animate + Animation(font_size=35)
        animate = animate + Animation(size_hint=(.5, .5), font_size=14, background_color=(1, 1, 0, 1), duration=1.5)
        animate = animate + Animation(pos_hint={'center_x': 1.1}, background_color=(0, 1, 1, 1))
        animate = animate + Animation(pos_hint={'center_x': 0.1}, background_color=(0, 0, 1, 1), duration=0.5)
        back = Animation(background_color=start_color, size_hint=start_size_h, pos_hint=start_pos_hint, font_size=start_font_size )

        self.animate = animate + back

    def start_animation(self):
        self.animate.start(self)


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
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThScr())
        sm.add_widget(FrScr())
        sm.add_widget(FvScr())
        txt = Label(text='Это надпись')
        btn = AnimatedButton(text='Нажми меня.', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5}, font_size = 22)
        btn.on_press = btn.start_animation 
                                     
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout


        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        

app = MyApp()
app.run()
