import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (500,700)
Builder.load_file("calc.kv")
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, n):
        if(self.ids.calc_input.text == "0" or self.ids.calc_input.text == "Error"):
            self.ids.calc_input.text = str(n)
        else:
            self.ids.calc_input.text += str(n)

    def operacion(self, simbolo):
        self.ids.calc_input.text += simbolo
    
    def eliminateLast(self):
        if(len(self.ids.calc_input.text) > 1):
            self.ids.calc_input.text = self.ids.calc_input.text[:-1]
        else:
            self.ids.calc_input.text = "0"

    def decimal(self):
        texto = self.ids.calc_input.text
        b = ["+","-","*","/","%"]
        a = len(texto) - 1
        while(True):
            if(a == -1 or texto[a] in b):
                texto += "."
                break
            if(texto[a] == "."):
                break
            a -= 1
        self.ids.calc_input.text = texto
    
    def cambiarsigno(self):
        if(self.ids.calc_input.text[0] == "-"):
            self.ids.calc_input.text = self.ids.calc_input.text[1:]
        else:
            menos = "-"
            self.ids.calc_input.text = menos + self.ids.calc_input.text

    def calcular(self):
        texto = self.ids.calc_input.text
        try:
            respuesta = eval(texto)
            self.ids.calc_input.text = str(respuesta)
        except:
            self.ids.calc_input.text = "Error"

class CalculadoraApp(App):
    def build(self):
        return MyLayout()

CalculadoraApp().run()