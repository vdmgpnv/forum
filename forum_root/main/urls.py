from django.urls import path
from .views import  create_thread, index, ThreadListView, thread_view


urlpatterns = [
    path('', index, name='index'),
    path('sections/<int:pk>', ThreadListView.as_view(), name='section'),
    path('thread/<int:pk>', thread_view, name='thread'),
    path('create_thread/<int:pk>', create_thread, name='create_th')
    
]
