from django.urls import path
from . import views

urlpatterns = [
    path('', views.tuman_list, name='tuman_list'),
    path('tuman/<int:tuman_id>/', views.maktab_list, name='maktab_list'),
    path('maktab/<int:maktab_id>/', views.oquvchi_list, name='oquvchi_list'),
    path('maktab/<int:maktab_id>/oquvchi/qoshish/', views.oquvchi_qoshish, name='oquvchi_qoshish'),
    path('oquvchi/<int:oquvchi_id>/tahrirlash/', views.oquvchi_tahrirlash, name='oquvchi_tahrirlash'),
    path('oquvchi/<int:oquvchi_id>/', views.oquvchi_detail, name='oquvchi_detail'),
    path('lists/', views.students_per_district, name='lists'),
]

