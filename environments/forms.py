from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'environment_name',
            'actions_number',
            'content',
            'gif_url',
        ]
        labels = {
            'title': 'Título',
            'environment_name': 'Ambiente',
            'actions_number': 'Número de ações',
            'content': 'Descrição do ambiente',
            'gif_url': 'URL do gif do ambiente',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }