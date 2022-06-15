import kivy
from kivy.app import App
from kivy.uix.button import Button

class PrimeCalculator(App):
    def build(self):
        return Button(text="Calculate Prime Numbers")

if __name__ == "__main__":
    PrimeCalculator().run()