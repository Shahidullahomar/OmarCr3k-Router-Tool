from kivy.app import App
from kivy.utils import platform
from kivy.uix.label import Label

# Wrap Android-only imports to prevent crashes on PC
if platform == 'android':
    from android.permissions import request_permissions, Permission
    from android import PythonService

class CameraApp(App):
    def build(self):
        if platform == 'android':
            # Request all necessary permissions at once
            request_permissions([
                Permission.CAMERA,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.FOREGROUND_SERVICE
            ])
            self.start_service()
        
        return Label(text="Background Service is Running...")

    def start_service(self):
        # Starts the service defined in buildozer.spec
        service = PythonService('Monitor', 'Service is running in background')
        service.start('service_args')

if __name__ == '__main__':
    CameraApp().run()
