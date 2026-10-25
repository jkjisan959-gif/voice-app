
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class VoiceChangerApp(App):
    def build(self):
        layout = FloatLayout()
        
        # স্ক্রিনে ভাসমান বাটন তৈরির ডিজাইন
        self.float_btn = Button(
            text='🎙️ Menu',
            size_hint=(None, None),
            size=(120, 120),
            pos_hint={'x': 0.8, 'y': 0.7},
            background_color=(0, 0.7, 0.9, 1)
        )
        self.float_btn.bind(on_press=self.open_menu)
        
        layout.add_widget(self.float_btn)
        return layout

    def open_menu(self, instance):
        # মেনু পপআপ যেখানে ভয়েস ফিল্টার সিলেক্ট করা যাবে
        content = FloatLayout()
        
        lbl = Label(text='Voice Modes:', pos_hint={'x': 0, 'y': 0.6}, size_hint=(1, 0.2))
        
        btn_male = Button(text='Male Voice', size_hint=(0.8, 0.15), pos_hint={'x': 0.1, 'y': 0.45})
        btn_female = Button(text='Female Voice', size_hint=(0.8, 0.15), pos_hint={'x': 0.1, 'y': 0.25})
        btn_funny = Button(text='Funny / Cartoon', size_hint=(0.8, 0.15), pos_hint={'x': 0.1, 'y': 0.05})
        
        btn_male.bind(on_press=lambda x: self.set_voice("Male Selected"))
        btn_female.bind(on_press=lambda x: self.set_voice("Female Selected"))
        btn_funny.bind(on_press=lambda x: self.set_voice("Funny Selected"))
        
        content.add_widget(lbl)
        content.add_widget(btn_male)
        content.add_widget(btn_female)
        content.add_widget(btn_funny)
        
        self.popup = Popup(title='Floating Voice Changer', content=content, size_hint=(0.8, 0.6))
        self.popup.open()

    def set_voice(self, mode):
        print(mode)
        self.popup.dismiss()

if __name__ == '__main__':
    VoiceChangerApp().run()
buildozer init

nano buildozer.spec


