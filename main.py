from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

Window.size = (480, 720)
Config.set('kivy', 'keyboard_mode', 'systemanddock')


def get_brutto(a, b, c):
    m = str((b / a) * 100 - 100)
    n = str((c / a) * 100 - 100)

    return m, n  # не треба тут словників


class Container(GridLayout):

    def calculate(self):
        try:
            a = int(self.a_input.text)
            b = int(self.ids.b_input.text)
            c = int(self.ids.c_input.text)
        
        except ValueError:
            ...  # додайте свою логіку, наприклад, виводьте повідомлення
            return  # щоб далі не рахувало

        except ...:
            ...  # додайте свою логіку, наприклад, виводьте повідомлення
            return  # щоб далі не рахувало

        try:
            m, n = get_brutto(a, b, c)
        except ZeroDivisionError:
            ...  # додайте свою логіку, наприклад, виводьте повідомлення
        
        self.result_a.text = str(a)
        self.result_m.text = str(m)
        self.result_n.text = str(n)


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
