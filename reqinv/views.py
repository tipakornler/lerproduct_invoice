from django.shortcuts import render
from django.views.generic.edit import CreateView
from reqinv.models import reqinv
from reqinv.forms import reqinvForm
from django.urls import reverse_lazy


class reqinvAllView(CreateView):
    model = reqinv
    form_class = reqinvForm
    template_name = 'reqinv/input.html'
    success_url = reverse_lazy('success')
    def test_func(self):
        return self.request
# Create your views here.

def success(request) :
    return render(request, 'reqinv/receiveform.html')