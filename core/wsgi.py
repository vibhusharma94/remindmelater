import os
from django.core.wsgi import get_wsgi_application
from core.libs.commons.utils import get_default_django_settings_module


os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
application = get_wsgi_application()
