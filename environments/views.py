from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm

class PostListView(generic.ListView):
    model = Post
    template_name = 'environments/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'environments/detail.html'

class PostSearchView(generic.ListView):
    model = Post
    template_name = 'environments/search.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '').lower()
        return Post.objects.filter(environment_name__icontains=query)

class PostCreateView(generic.CreateView):
    model = Post
    fields = [
        'title',
        'environment_name',
        'actions_number',
        'content',
        'gif_url',
    ]
    template_name = 'environments/create.html'

    def get_success_url(self):
        return reverse('environments:detail', kwargs={'pk': self.object.pk})

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = [
        'title',
        'environment_name',
        'actions_number',
        'content',
        'gif_url',
    ]
    template_name = 'environments/update.html'

    def get_success_url(self):
        return reverse('environments:detail', kwargs={'pk': self.object.pk})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'environments/delete.html'

    def get_success_url(self):
        return reverse('environments:index')

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('environments:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'environments/comment.html', context)