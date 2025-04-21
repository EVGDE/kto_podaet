
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PingPongApp(App):
    def build(self):
        self.title = "Кто подаёт, настольный теннис"

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.player1_input = TextInput(hint_text='Имя игрока 1', multiline=False)
        self.player2_input = TextInput(hint_text='Имя игрока 2', multiline=False)
        self.score1_input = TextInput(hint_text='Счёт игрока 1 (целое число)', input_filter='int', multiline=False)
        self.score2_input = TextInput(hint_text='Счёт игрока 2 (целое число)', input_filter='int', multiline=False)
        self.starter_input = TextInput(hint_text='Кто начинал подачу (имя)', multiline=False)

        self.button = Button(text='Кто подаёт?', size_hint=(1, 0.3))
        self.button.bind(on_press=self.check_server)
        self.result_label = Label(text='', halign='center')

        for widget in [self.player1_input, self.player2_input,
                       self.score1_input, self.score2_input,
                       self.starter_input, self.button, self.result_label]:
            self.layout.add_widget(widget)

        return self.layout

    def check_server(self, instance):
        try:
            p1 = self.player1_input.text.strip()
            p2 = self.player2_input.text.strip()
            s1 = int(self.score1_input.text.strip())
            s2 = int(self.score2_input.text.strip())
            starter = self.starter_input.text.strip()

            if starter not in [p1, p2]:
                raise ValueError("Начальный подающий должен быть одним из игроков.")

            current = self.get_current_server(p1, p2, s1, s2, starter)
            self.result_label.text = f"Сейчас подаёт: {current}"
        except Exception as e:
            self.result_label.text = f"[Ошибка] {str(e)}"

    def get_current_server(self, player1, player2, score1, score2, starting_server):
        total_points = score1 + score2
        switches = total_points // 2
        return starting_server if switches % 2 == 0 else (player2 if starting_server == player1 else player1)

if __name__ == '__main__':
    PingPongApp().run()
