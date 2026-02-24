from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark/<int:student_id>/<str:status>/', views.mark_attendance, name='mark'),
    path('records/', views.view_attendance, name='records'),
]