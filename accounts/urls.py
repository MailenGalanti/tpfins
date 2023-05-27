from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ... otras rutas ...
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', views.profile, name='profile'),

]
