from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicNamesApp():
    names = ('Jack', 'John', 'Jonathan', 'Jade', 'Jazmin')

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Names"
        self.root = Builder.load_file('dynamic_names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

DynamicNamesApp().run()