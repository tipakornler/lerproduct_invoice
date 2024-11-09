from django.shortcuts import render
from adminquestion.models import Question
from django.views.generic import ListView, DetailView ,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F

class QuestionListView(LoginRequiredMixin,ListView):
    model = Question
    paginate_by = 20
    def get_queryset(self):
        qa = self.request.GET.get('qa') 
        ans = self.request.GET.get('ans')
        kwargs = {}
        if qa :
            kwargs.update({'{0}__{1}'.format('question', 'icontains'): qa})
        if len(kwargs) >0:
            question = Question.objects.filter(Q(question__icontains = qa) | Q(answer__icontains = qa)) 
        else:
            question = Question.objects.all()
        return question
# Create your views here.
