from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, EmailVerificationView, PasswordRecoveryView, LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

]
