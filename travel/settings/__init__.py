from .production import *
try:
    from .local_settings import *
except ImportError:
    pass

from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(
        'accounts/password_reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        'accounts/password_reset_done/',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    url(
        'accounts/password_reset_confirm/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        'accounts/password_reset_complete/',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
