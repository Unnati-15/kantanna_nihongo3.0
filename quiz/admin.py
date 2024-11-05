from django.contrib import admin
from . import models

admin.site.register(models.QuizType)
admin.site.register(models.QuizQuestion)
admin.site.register(models.UserSubmittedAnswer)