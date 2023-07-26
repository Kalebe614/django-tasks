from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
            return render(request, self.template_name)