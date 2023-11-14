from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, EmailVerifyView, UserFormView, create_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/', EmailVerifyView.as_view(), name='verify_email'),
    path('user_form/', UserFormView.as_view(), name='user_form'),
    path('user_form/create_new_password/', create_new_password, name='create_new_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
