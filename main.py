from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class DynamicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # 🔗 الرابط السحري الخاص بك (GitHub Pages)
        self.MY_CLOUD_URL = "https://github.io"
        
        # تشغيل المتصفح بأمان بعد جزء من ثانية من إقلاع التطبيق لمنع أي تعليق
        Clock.schedule_once(self.open_webview, 0.5)
        
        return layout

    def open_webview(self, dt):
        try:
            # استدعاء الجافا المدمجة في الأندرويد لفتح الرابط بكامل الشاشة بطريقة مستقرة
            from jnius import autoclass
            import android
            
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            
            # فتح الرابط عبر متصفح النظام الافتراضي كـ تظهير فوري
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(self.MY_CLOUD_URL))
            PythonActivity.mActivity.startActivity(intent)
        except Exception:
            # للتشغيل والتجربة على الكمبيوتر بدون أخطاء
            import webbrowser
            webbrowser.open(self.MY_CLOUD_URL)

if __name__ == "__main__":
    DynamicApp().run()
