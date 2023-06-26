from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "metropark_01.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import metropark_01.users.signals  # noqa: F401
        except ImportError:
            pass
