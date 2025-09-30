from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.label = Label(text="Enter your name:")
        self.input = TextInput(multiline=False)
        btn = Button(text="Say Hello")

        btn.bind(on_press=self.say_hello)

        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)

        return layout

    def say_hello(self, instance):
        self.label.text = f"Hello, {self.input.text}!"

if __name__ == "__main__":
    MyApp().run()
