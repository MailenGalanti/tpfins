"""
URL configuration for tpfins project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from website.views import ContactCreateView, BenchmarkCreateView, success_messages, BenchmarkListView, BenchmarkDeleteView, BenchmarkDetailView, BenchmarkUpdateView
from accounts.views import profile

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("contact/", ContactCreateView.as_view(), name="contact_us"),
    path("benchmark/", BenchmarkCreateView.as_view(), name="benchmark_request"),
    path('accounts/profile/', profile, name='profile'),
    path('benchmarks/', BenchmarkListView.as_view(), name='benchmark_list'),
    path('benchmark/<int:pk>/delete/', BenchmarkDeleteView.as_view(), name='benchmark_delete'),
    path('benchmark/<int:pk>/', BenchmarkDetailView.as_view(), name='benchmark_detail'),    
    path('benchmark/<int:pk>/edit/', BenchmarkUpdateView.as_view(), name='benchmark_edit'),

    path('accounts/logout/', LogoutView.as_view(next_page='inicio'), name='logout'),

    path("", success_messages, name="success_messages"),
]
