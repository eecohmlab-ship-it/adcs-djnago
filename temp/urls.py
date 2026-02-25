
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student/', views.student_list, name='student_list'),
    path('student/add/', views.student_entry, name='student_entry'),
    path('student/update/<int:pk>/', views.student_update, name='student_update'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),  
]