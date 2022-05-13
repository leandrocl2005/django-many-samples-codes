from django.apps import AppConfig


class UsersHubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_hub'

    def ready(self):
        import users_hub.signals
