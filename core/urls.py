from django.urls import path
from core import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='login.html')),
]