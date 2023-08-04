from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import TaskModel
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .utils import filter_and_order_tasks


@method_decorator(login_required, name='dispatch')
class TaskView(ListView):
    template_name = 'task.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_sort_option'] = self.request.GET.get('filter', 'added')
        return context

    def get_queryset(self):

        filter_option = self.request.GET.get('filter')
        sort_option = self.request.GET.get('sort')

        queryset = TaskModel.objects.filter(user=self.request.user)
        return filter_and_order_tasks(queryset, filter_option, sort_option)
       

class TaskCreateView(CreateView):
    template_name = 'task.html'
    model = TaskModel
    fields = ['description', 'dueDate']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,'Task created successfully')
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    template_name = 'task.html'
    model = TaskModel
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'Task deleted successfully')
        return response

class TaskUpdateCompletedView(UpdateView):
    template_name = 'task.html'
    model = TaskModel
    success_url = reverse_lazy('task')
    fields = ['completed', 'dueDate']
   
    def form_valid(self, form):
            if form.cleaned_data['completed']:
                form.instance_dueDate = None

            response = super().form_valid(form)
            messages.success(self.request,'Task updated successfully')
            return response

class TaskUpdateView(UpdateView):
    template_name = 'task.html'
    model = TaskModel
    success_url = reverse_lazy('task')
    fields = ['description', 'dueDate','completed'] 

    def form_valid(self, form):
        if form.cleaned_data['dueDate']:
            form.instance_completed = True

        response = super().form_valid(form)
        messages.success(self.request, 'Task updated successfully')
        return response
    
