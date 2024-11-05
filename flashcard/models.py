from django.db import models
from django.contrib.auth.models import User

class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fc_name = models.CharField(max_length=100)
    fc_description = models.TextField(max_length=800)

    class Meta:
        verbose_name_plural='FlashCard'

    def __str__(self) :
        return self.fc_name

