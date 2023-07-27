from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import TaskModel
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import ListView, DetailView

@method_decorator(login_required, name='dispatch')
class TaskView(ListView):
    template_name = 'task.html'
    model = TaskModel
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user)
