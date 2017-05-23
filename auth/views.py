from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from TsCh.settings import LOGIN_URL


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = LOGIN_URL

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

from django.contrib.auth.views import logout


def my_logout(request):
    logout(request)
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("/logout2/")
