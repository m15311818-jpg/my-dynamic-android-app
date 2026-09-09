from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class DynamicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # 🔗 رابط التحكم مكتوب في قلب كود التطبيق الأساسي
        self.MY_CLOUD_URL = "https://github.io"
        Clock.schedule_once(self.open_webview, 0.2)
        return layout

    def open_webview(self, dt):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            
            # فتح الرابط مباشرة من قلب نظام أندرويد
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(self.MY_CLOUD_URL))
            PythonActivity.mActivity.startActivity(intent)
        except Exception:
            import webbrowser
            webbrowser.open(self.MY_CLOUD_URL)

if __name__ == "__main__":
    DynamicApp().run()
