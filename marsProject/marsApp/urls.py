from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stage1/', views.application_stage1, name='application_stage1'),
    path('stage2/', views.application_stage2, name='application_stage2'),
    path('stage3/', views.application_stage3, name='application_stage3'),
]
