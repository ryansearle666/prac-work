"""
Basic Kivy test code
If this works, it will produce a GUI window with "hello world" in the middle
and you know you have set everything up correctly.
It also prints the Python version in the run output (may be mixed in with Kivy output)
The Python version should be 3.x (not 2.x).
"""
#
# from kivy.app import App
# from kivy.uix.button import Button
# import sys
#
#
# class CheckSetupApp(App):
#
#     def build(self):
#         return Button(text='hello world')
#
#
# if __name__ == '__main__':
#     # In PyCharm, right-click here and choose 'Run check_setup'
#     print("Python version information:", sys.version)
#     CheckSetupApp().run()


"""From Scratch Exercise
Kivy GUI program to convert m to km
"""

from kivy.app import App
from kivy.lang import Builder

conversion_factor = 1.609

class ConvertMToKm(App):
    """ConvertMToKm is a Kivy app that converts values in Miles to Kilometres"""
    def build(self):
        """Build app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self):
        """Convert Miles to Kilometres"""
        value = self.get_valid_input()
        result = value * conversion_factor
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, addorsub):
        """changes input_distance by + or - 1"""
        value = self.get_valid_input() + addorsub
        self.root.ids.input_distance.text = str(value)
        self.handle_calculate()

    def get_valid_input(self):
        """Error check input for invalid values"""
        try:
            value = float(self.root.ids.input_distance.text)
            return value
        except:
            return 0.0

ConvertMToKm().run()


