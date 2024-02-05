from django.apps import AppConfig


class MyOrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_orm'
