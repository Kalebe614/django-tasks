from django.urls import path
from task import views
urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
]
