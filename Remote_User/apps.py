from django.apps import AppConfig


class RemoteUserConfig(AppConfig):
    name = 'Remote_User'


INSTALLED_APPS = [
    # ... other apps ...
    'Remote_User',
]