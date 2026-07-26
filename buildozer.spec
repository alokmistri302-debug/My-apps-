[app]

# (str) Title of your application
title = My Python App

# (str) Package name
package.name = mypythonapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# यहाँ अपने ऐप की जरूरत के हिसाब से लाइब्रेरी लिखें (कम से कम python3 और kivy होना जरूरी है)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
