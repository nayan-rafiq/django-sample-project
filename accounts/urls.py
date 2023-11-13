from django.urls import path, re_path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("register", views.signup_user, name="register"),
    path("register/success", TemplateView.as_view(template_name="accounts/registration_successful.html"),
         name="signup_success"),
    re_path('activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)', views.verify_email_view, name='activate_user'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_view, name='logout_user'),
    path('profile', views.user_profile, name='user_profile'),
    path("password/forgot", views.forgot_password_view, name='reset-password'),
    path("password/reset/requested", TemplateView.as_view(template_name="accounts/passwords/reset_requested.html"),
         name='password_reset_requested'),
    re_path("password/set/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)", views.set_password_view,
            name='set_password_view'),
    path("password/reset/complete", TemplateView.as_view(template_name="accounts/passwords/reset_complete.html"),
         name='password_reset_complete'),
]
