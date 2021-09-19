from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App

Window.size = (400,600)



Builder.load_file('cal.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.input_label.text = '0'

    def num_press(self,button):

        prior = self.ids.input_label.text
        if "Error" in prior:
            prior = ''

        if prior == "0":
            self.ids.input_label.text = ''
            self.ids.input_label.text = f'{button}'
        else:
            self.ids.input_label.text = f'{prior}{button}'

    def operator(self,sign):
        prior = self.ids.input_label.text
        self.ids.input_label.text = f'{prior}{sign}'

    def dot(self):
        prior = self.ids.input_label.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
             self.ids.input_label.text = f'{prior}.'

        elif "." in prior:
            pass
        else:
            self.ids.input_label.text = f'{prior}.'

    def equal(self):
        try:
            prior = self.ids.input_label.text
            answer = eval(prior)
            self.ids.input_label.text = str(answer)
        except:
            self.ids.input_label.text = 'Error'
        '''
        if "+" in prior:
            num_list = prior.split('+')
            answer = 0.0
            for num in num_list:
                answer = answer + float(num)

        self.ids.input_label.text = str(answer)
        '''

    def remove(self):
        prior = self.ids.input_label.text
        prior = prior[:-1]
        self.ids.input_label.text = f'{prior}'

    def plusmin(self):
        prior = self.ids.input_label.text
        if "-" in prior:
           self.ids.input_label.text = f'{prior.replace("-","")}'
        else:
           self.ids.input_label.text = f'-{prior}'

class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()