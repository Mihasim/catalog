from random import randint

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    """
    Регистрация и отправка на почту ключа
    """
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verify_email')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        new_user.save()
        send_mail(
            subject='Подтвердите регистрацию',
            message=f'Вы зарегистрировались, теперь подтвердите резистрацию\n '
                    f'http://127.0.0.1:8000/verify_email/\n'
                    f'{new_user.key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        return super().form_valid(form)


class EmailVerifyView(TemplateView):
    """
    Проверка ключа регистрации, если ключ совпадает то пользователь прошел верификацию
    """
    template_name = 'users/verify_email.html'

    def post(self, request):
        key = request.POST.get('key')
        user_code = User.objects.filter(key=key).first()

        if user_code is not None and user_code.key == key:
            user_code.email_verify = True
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        else:
            user_code.is_active = False
            return redirect('users:verify_email')


class UserFormView(UpdateView):
    model = User
    success_url = reverse_lazy('users:user_form')
    fields = '__all__'

    def get_object(self, queryset=None):
        return self.request.user


def create_new_password(request):
    """
    Смена пароля и отправка на почту нового пароля
    """
    new_password = ''.join([str(randint(0, 9)) for i in range(8)])
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Новый пароль',
        message=f'{new_password}\n ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    return redirect(reverse('users:login'))
