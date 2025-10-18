from django.urls import path

from port import views



urlpatterns = [
  path('', views.PostView.as_view(), name='home')
]