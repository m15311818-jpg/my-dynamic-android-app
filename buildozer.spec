[app]
# (str) Title of your application
title = My Dynamic App

# (str) Package name
package.name = dynamicapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تم تبسيطها تماماً لتتوافق مع بيئة البناء وتمنع تضارب النسخ
requirements = python3,kivy,android

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen or not
fullscreen = 1

# (list) Permissions
# تصريح الإنترنت الإجباري لفتح رابطك
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Log level (2 = debug with full output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
