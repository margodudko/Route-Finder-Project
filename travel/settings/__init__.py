from .production import *
try:
    from .local_settings import *
except ImportError:
    pass

from django.urls import reverse_lazy

