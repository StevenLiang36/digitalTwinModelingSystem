from django.apps import AppConfig


class PreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Pre"

    def ready(self):
        import Pre.signals
