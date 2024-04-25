from django.apps import AppConfig


class LostObjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lost_objects"
    verbose_name = 'Реестр пропавших, утраченных, похищенных культурных ценностей'
