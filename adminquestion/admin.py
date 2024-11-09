from django.contrib import admin
from adminquestion.models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
