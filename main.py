from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import webbrowser

class DynamicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # 🔗 رابط شاشتك الزرقاء الحقيقي في قلب الكود
        self.MY_CLOUD_URL = "https://github.io"
        
        # فتح الرابط فوراً عند إقلاع التطبيق بأسرع وأبسط طريقة للأندرويد
        Clock.schedule_once(self.open_link, 0.2)
        return layout

    def open_link(self, dt):
        webbrowser.open(self.MY_CLOUD_URL)

if __name__ == "__main__":
    DynamicApp().run()
