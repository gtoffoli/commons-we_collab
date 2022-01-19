
from django.apps import AppConfig
import commons

class WecollabConfig(AppConfig):
    name = 'we_collab'

    def ready(self):
        import commons.signal_handlers
