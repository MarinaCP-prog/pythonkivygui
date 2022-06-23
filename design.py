from sqlite3 import Row
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    colour = ObjectProperty(None)
    
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text
        
        print(f'Hello {name}, you like {pizza} pizza and your favorite colour is {colour}.') 
        # Print it to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favorite colour is {colour}.'))
        
        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()   