[app]

# (str) Title of your application
title = VoiceChanger

# (str) Package name
package.name = voicechanger

# (str) Package domain (needed for android packaging)
package.domain = org.voice

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3,kivy,android

# (int) Android API level to target
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) Permissions
android.permissions = INTERNET
