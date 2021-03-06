from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required

from account.views import SignupView, LoginView, LogoutView
from account.views import ConfirmEmailView
from account.views import ChangePasswordView, PasswordResetView, PasswordResetDoneView, PasswordResetKeyView
from account.views import SettingsView


urlpatterns = patterns("",
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^login/$", LoginView.as_view(), name="account_login"),
    url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    url(r"^password/reset/done/$", PasswordResetDoneView.as_view(), name="account_password_reset_done"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", PasswordResetKeyView.as_view(), name="account_password_reset_key"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
)
