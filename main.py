from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle

class PianoApp(App):
    def build(self):
        # 1. التنسيق الرئيسي للتطبيق مع خلفية نيون مميزة جداً
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        
        with main_layout.canvas.before:
            # دمج اللون البنفسجي الغامق مع النيون لمظهر جذاب جداً على المتجر
            Color(0.08, 0.05, 0.18, 1) 
            self.rect = Rectangle(size=(2000, 4000), pos=(0,0))
            
        # عنوان التطبيق الأنيق
        title = Label(
            text="✨ NEON PIANO PRO ✨", 
            font_size='28sp', 
            bold=True, 
            color=(0, 1, 0.8, 1), # لون فيروزي مضيء
            size_hint_y=0.15
        )
        main_layout.add_widget(title)
        
        # 2. منطقة أزرار البيانو (الأزرار البيضاء)
        piano_keys_layout = BoxLayout(orientation='horizontal', spacing=4, size_hint_y=0.8)
        
        # النغمات الأساسية السبعة (C, D, E, F, G, A, B)
        notes = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
        
        # إنشاء الأزرار بشكل أنيق جداً يناسب المتجر
        for note in notes:
            btn = Button(
                text=note,
                font_size='18sp',
                bold=True,
                color=(0.1, 0.1, 0.1, 1),
                background_normal='', # إزالة الشكل الافتراضي لتطبيق التصميم الخاص بنا
                background_color=(0.95, 0.95, 0.95, 1), # أزرار بيضاء ناصعة
                border=(10, 10, 10, 10)
            )
            # ربط الزر بأمر العزف عند الضغط
            btn.bind(on_press=lambda instance, n=note: self.play_note(n))
            piano_keys_layout.add_widget(btn)
            
        main_layout.add_widget(piano_keys_layout)
        return main_layout

    def play_note(self, note):
        # توليد الصوت الذكي المدمج (تنبيه أو نغمة سريعة لضمان سرعة البناء)
        try:
            from android.media import AudioManager, ToneGenerator
            # استخدام المولد الصوتي الرسمي للأندرويد لعزف النغمات بنقاء وبدون ملفات خارجية
            tone_gen = ToneGenerator(AudioManager.STREAM_MUSIC, 100)
            # نغمات مختلفة بناءً على الزر المضغوط
            tone_mapping = {'Do': 1, 'Re': 2, 'Mi': 3, 'Fa': 4, 'Sol': 5, 'La': 6, 'Si': 7}
            tone_gen.startTone(tone_mapping.get(note, 1), 200) # عزف لمدة 200 ملي ثانية
        except ImportError:
            # لو شغال على الكمبيوتر للتجربة
            print(f"🎵 Playing note: {note}")

if __name__ == '__main__':
    PianoApp().run()
