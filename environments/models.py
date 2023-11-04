from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=30)
    environment_name = models.CharField(max_length=25) # nome do ambiente escolhido pelo usuário para o post
    actions_number = models.IntegerField(default=0) # número de ações disponíveis no ambiente
    content = models.TextField(default="")
    creation_date = models.DateTimeField(default=timezone.now)
    gif_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} (Ambiente: {self.environment_name})'