from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm

class PostListView(generic.ListView):
    model = Post
    template_name = 'environments/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ambientes'
        context['envpage_title'] = 'Encontre o ambiente ideal'
        context['category'] = False
        return context

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
    form_class = PostForm
    template_name = 'environments/create.html'

    def get_success_url(self):
        return reverse('environments:detail', kwargs={'pk': self.object.pk})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
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

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'environments/categories.html'

class CategoryPostsListView(generic.ListView):
    template_name = 'environments/index.html'
    context_object_name = 'post_list'

    def get_category(self):
        return Category.objects.get(pk=self.kwargs['category_id'])

    def get_queryset(self):
        return self.get_category().posts.all()
    
    def get_context_data(self, **kwargs):
        category = self.get_category()
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Categoria'
        context['envpage_title'] = f'Categoria {category.name}'
        context['category'] = True
        context['category_id'] = category.id
        return context

class CategoryPostDetailView(generic.DetailView):
    model = Post
    template_name = 'environments/detail.html'

    def get_object(self):
        category_id = self.kwargs.get('category_id')
        pk = self.kwargs.get('pk')
        category = Category.objects.get(pk=category_id)
        posts = category.posts.all()
        post = get_object_or_404(posts, pk=pk) 
        return post

