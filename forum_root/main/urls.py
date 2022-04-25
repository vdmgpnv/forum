from django.urls import path

from .views import index, register, AnotherLogoutview


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('logout/', AnotherLogoutview.as_view(), name='logout')
]
