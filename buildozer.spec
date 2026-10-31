[app]

# (str) Title of your application
title = Ezan Vakti

# (str) Package name
package.name = ezanvakti

# (str) Package domain (needed for android packaging)
package.domain = org.seco

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = bin, venv, .git, .github

# (list) List of inclusions
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Specify python modules here
requirements = python3,kivy

# (list) Custom source folders for requirements
#requirements.source.dir = ../relative/path/to/source/fold

# (list) Presplash graphics
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Icon graphics
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations
orientation = portrait

# (list) List of services
#services = NAME:ENTRYPOINT_TO_PYTHON,NAME2:ENTRYPOINT2_TO_PYTHON

#
# OSX Specific
#

#
# Android specific
#

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 20

# (str) OPTS to pass to adb
#android.adb_args = -s emulator-5554

# (list) python-for-android branch
#p4a.branch = master

# (str) Bootstrap to use for android build
#p4a.bootstrap = sdl2

# (list) The format used to package the app for store ('apk' or 'aab')
android.package_format = apk


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, storage, sdk etc.
#build_dir = .buildozer

# (str) Path to build output (where the APK is)
bin_dir = bin
