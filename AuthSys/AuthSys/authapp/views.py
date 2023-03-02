from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views, login

from AuthSys.authapp.forms import CreateProfileForm
from AuthSys.authapp.models import UserProfile


class IndexView(views.View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'index.html')


class DashboardView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = UserProfile
    template_name = 'dashboard.html'


class RegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse_lazy('dashboard', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('dashboard')  # or can reverse_lazy('details')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class LogOutView(auth_views.LogoutView):
    pass