[app]

title = Manou Social
package.name = manousocial
package.domain = org.manou

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.androidx = True

# إجبار البناء على مسار الـ SDK الصحيح وتجنب أي خطأ في الإصدارات
android.sdk_path = /usr/local/lib/android/sdk

[buildozer]
log_level = 2
warn_root = 1
