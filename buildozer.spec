[app]

# (str) Title of your application
title = Manou Social

# (str) Package name
package.name = manousocial

# (str) Package domain (needed for android packaging)
package.domain = org.manou

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source directories to include
source.include_dirs = 

# (list) Application requirements
requirements = python3,kivy

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use.
android.ndk_api = 21

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (list) The Android archs to build for
android.archs = arm64-v8a

