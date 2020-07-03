from django.urls import path
from . import views

urlpatterns = [
    path('', views.base , name='base'),
    path('generate',views.generate,name='generate'),
    path('generate2',views.generate2,name='generate2'),
    path('generate3',views.generate3,name='generate3'),
    path('login',views.login,name='login'),
    path('lr',views.lr,name='lr'),
    path('reg',views.reg,name='reg'),
    path('areg',views.areg,name='areg'),
    path('log',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('combination',views.combination,name='combination'),

]
