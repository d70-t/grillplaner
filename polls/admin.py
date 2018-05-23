from django.contrib import admin

from .models import Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'attends', 'count', 'brings', 'email')
    list_filter = ('attends',)

admin.site.register(Answer, AnswerAdmin)
