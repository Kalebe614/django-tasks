from django.urls import path
from task import views
urlpatterns = [
   path('', views.TaskView.as_view(), name='task'),
   path('create/', views.TaskCreateView.as_view(), name='create'),
]
