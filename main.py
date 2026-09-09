from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class DynamicApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # 🔗 استبدل هذا الرابط بالرابط الخاص بك الذي حصلت عليه من GitHub Pages
        MY_CLOUD_URL = "https://github.io" 
        
        try:
            # استدعاء الـ WebView المدمج في الأندرويد لفتح الرابط بكامل الشاشة
            from android.webview import WebView
            WebView(MY_CLOUD_URL)
        except ImportError:
            # كود احتياطي لفتح المتصفح لو جربت الكود على الكمبيوتر
            import webbrowser
            webbrowser.open(MY_CLOUD_URL)
            
        return layout

if __name__ == "__main__":
    DynamicApp().run()
