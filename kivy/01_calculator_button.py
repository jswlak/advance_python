#GridLayout (Calculator-like buttons)
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=3, spacing=10, padding=10)

        for i in range(1, 10):
            layout.add_widget(Button(text=str(i)))

        return layout

if __name__ == "__main__":
    MyApp().run()
