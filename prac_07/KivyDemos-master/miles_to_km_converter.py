from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

# from kivy.core.window import Window

MILES_TO_KM = 1.6


class miles_to_km(App):
    km_from_miles = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km_converter.kv')
        return self.root

    def calculate_km_from_miles(self):
        number_to_calculate = self.get_miles()
        self.km_from_miles = str(number_to_calculate * MILES_TO_KM)

    def handle_increment(self, increment):
        number_to_calculate = self.get_miles() + increment
        self.root.ids.number_received.text = str(number_to_calculate)
        self.calculate_km_from_miles()

    def get_miles(self):
        try:
            number_to_calculate = float(self.root.ids.number_received.text)
            return number_to_calculate
        except ValueError:
            return 0


miles_to_km().run()
