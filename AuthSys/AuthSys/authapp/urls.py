from django.urls import path

from AuthSys.authapp.views import IndexView, RegisterView, DashboardView, LogOutView, LoginView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),

    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout'),

    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
)