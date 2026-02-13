from django.contrib import admin
from django.urls import path
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student-entry/', views.student_entry, name='student_entry'),
    path('student-list/', views.student_list, name='student_list'),                            
]
