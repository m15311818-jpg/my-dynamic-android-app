[app]
title = My Dynamic App
package.name = dynamicapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 🎯 السر هنا: حددنا النسخ المستقرة للأندرويد لمنع أي خطأ تلقائي
requirements = python3,kivy==2.3.0,android

orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# ⚙️ إعدادات الأدوات المقفلة المضمونة
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

log_level = 2
warn_on_root = 1
