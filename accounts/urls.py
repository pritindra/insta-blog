from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password-reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password-reset-done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password-reset-confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password-reset-complete")
]