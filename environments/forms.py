from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
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
    
    def clean_gif_url(self):
        gif_url = self.cleaned_data.get('gif_url')

        if gif_url and not gif_url.startswith('https://gymnasium'):
            raise forms.ValidationError('O gif deve ser de um ambiente do gymnasium.')

        return gif_url

class CommentForm(forms.ModelForm):
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