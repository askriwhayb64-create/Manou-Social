[app]

# (str) Title of your application
title = Manou Social

# (str) Package name
package.name = manousocial

# (str) Package domain (needed for android packaging)
package.domain = org.manou

# (str) Source files where the let's go is (relative to directory of this file)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (str) Explicitly force SDK and NDK paths to avoid version mismatch
# android.sdk_path = /usr/local/lib/android/sdk
# android.ndk_path = 

# (list) Android architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Use AndroidX
android.androidx = True

[buildozer]
log_level = 2
warn_root = 1




