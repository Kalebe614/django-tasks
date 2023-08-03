from django.urls import path
from task import views

urlpatterns = [
   path('', views.TaskView.as_view(), name='task'),
   path('create/', views.TaskCreateView.as_view(), name='create'),
   path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
   path('updateCompleted/<int:pk>/', views.TaskUpdateCompletedView.as_view(), name='updateCompleted'),
   path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
]
