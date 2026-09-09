[app]
title = My Dynamic App
package.name = dynamicapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 🎯Requirements خفيفة جداً بدون أي مكتبات جافا خارجية
requirements = python3,kivy,android

orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.archs = arm64-v8a
log_level = 2
