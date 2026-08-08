[app]

# (str) Title of your application
title = Manou Social

# (str) Package name
package.name = manousocial

# (str) Package domain (needed for android packaging)
package.domain = org.manou

# (str) Source files where the let's go is (relative to directory of this file)
source.dir = .

# (list) Source files to include (let's include png, jpg, kv, atlas)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_pattern = assets/*.pngimages/images/*.jpg

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid orientations: landscape, portrait, all or reverse-landscape/reverse-portrait
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (list) Android architecture to build for, can be armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Use AndroidX
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning instead of aborting when dalvik VM-check fails
warn_root = 1

