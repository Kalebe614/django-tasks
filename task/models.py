from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class TaskModel(models.Model):
    created = models.DateTimeField('Created',auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    description = models.CharField('Description',max_length=100)
    completed = models.BooleanField('Completed', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = ('description')
        verbose_name_plural = ('descriptions')

