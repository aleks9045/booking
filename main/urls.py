from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('krasnodar', views.krasnodar, name='krasnodar'),
    path('sochi', views.sochi, name='sochi'),
    path('rostov_on_don', views.rostov_on_don, name='rostov_on_don'),
    path('yakutsk', views.yakutsk, name='yakutsk'),
    path('moscow', views.moscow, name='moscow'),
    path('saintpetersburg', views.saintpetersburg, name='saintpetersburg'),
    path('yalta', views.yalta, name='yalta'),
    path('krim', views.krim, name='krim'),
    path('ekaterinburg', views.ekaterinburg, name='ekaterinburg'),
    path('registration', views.registration, name='registration'),
    path('booking', views.booking, name='booking')
]
