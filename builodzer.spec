# (list) Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, FOREGROUND_SERVICE, RECEIVE_BOOT_COMPLETED

# (list) Services to create
# Format: Name:File.py
services = Monitor:service.py

# (list) Application requirements
requirements = python3, kivy, requests, pyjnius, android
