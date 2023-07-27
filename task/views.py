from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import TaskModel
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
@method_decorator(login_required, name='dispatch')
class TaskView(ListView):
    template_name = 'task.html'
    model = TaskModel
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user)

class TaskCreateView(CreateView):
    template_name = 'task.html'
    model = TaskModel
    fields = ['description']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,'Task created successfully')
        return super().form_valid(form)

