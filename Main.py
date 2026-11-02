from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime

class FatimaJarvisApp(App):
    def build(self):
        # مین لے آؤٹ
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # ٹائتل لیبل
        self.title_label = Label(
            text='[b]Fatima JARVIS AI[/b]',
            markup=True,
            font_size=28,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.title_label)
        
        # ڈسپلے سکرین (جواب دکھانے کے لیے)
        self.output_label = Label(
            text='السلام علیکم! میں فاطمہ جاروس ہوں۔ آپ کی کیا مدد کر سکتی ہوں؟',
            font_size=18,
            size_hint=(1, 0.5),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.output_label)
        
        # یوزر ان پٹ باکس
        self.user_input = TextInput(
            text='',
            hint_text='یہاں اپنا حکم درج کریں...',
            size_hint=(1, 0.15),
            multiline=False
        )
        layout.add_widget(self.user_input)
        
        # کمانڈ بھیجنے کا بٹن
        submit_btn = Button(
            text='حکم دیں (Send)',
            size_hint=(1, 0.15),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        submit_btn.bind(on_press=self.process_command)
        layout.add_widget(submit_btn)
        
        return layout

    def process_command(self, instance):
        text = self.user_input.text.lower()
        
        if 'time' in text or 'وقت' in text:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            self.output_label.text = f'اس وقت وقت ہو رہا ہے: {current_time}'
        elif 'hello' in text or 'hi' in text or 'السلام' in text:
            self.output_label.text = 'وعلیکم السلام! فرمائیے، میں حاضر ہوں۔'
        elif 'name' in text or 'نام' in text:
            self.output_label.text = 'مرا نام فاطمہ جاروس (Fatima JARVIS AI) ہے!'
        else:
            self.output_label.text = f'آپ نے کہا: "{self.user_input.text}" - یہ فی الحال میرے سسٹم میں سیٹ نہیں ہے۔'
        
        self.user_input.text = ''

if __name__ == '__main__':
    FatimaJarvisApp().run()
  
