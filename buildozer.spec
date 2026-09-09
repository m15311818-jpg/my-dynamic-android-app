[app]

# (str) Title of your application
title = My Dynamic App

# (str) Package name
package.name = dynamicapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# تم ضبط الإصدارات بدقة هنا لضمان التوافق التام مع خوادم جيتهاب ومنع أي أخطاء
requirements = python3==3.10.12,hostpython3==3.10.12,kivy,android,pyjnius>=1.5.0

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen or not
fullscreen = 1

# (list) Permissions
# تصريح الإنترنت ضروري جداً لكي يتصل التطبيق بالرابط الخاص بك
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow service to use the same process as the main activity
android.meta_data =

# (list) The Android archs to build for
# لضمان عمل التطبيق على الهواتف الحديثة والقديمة
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
