from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('update-student/<int:pk>/', views.update_student, name='update_student'),  # Update URL
    path('delete-student/<int:pk>/', views.delete_student, name='delete_student'),  # Delete URL
]
