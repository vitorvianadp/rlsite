from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def list_environment_posts(request):
    posts_list = Post.objects.all()
    context = {"posts_list": posts_list}
    return render(request, 'environments/index.html', context)

def detail_environment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'environments/detail.html', context)

def search_environment_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        posts_list = Post.objects.filter(environment_name__icontains=search_term)
        context = {"posts_list": posts_list}
    return render(request, 'environments/search.html', context)

def create_environment_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            environment_name = form.cleaned_data['environment_name']
            actions_number = form.cleaned_data['actions_number']
            content = form.cleaned_data['content']
            gif_url = form.cleaned_data['gif_url']
            post = Post(title=post_title,
                        environment_name=environment_name,
                        actions_number=actions_number,
                        content=content,
                        gif_url=gif_url)
            post.save()
            return HttpResponseRedirect(
                reverse('environments:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'environments/create.html', context)
    
def update_environment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.environment_name = form.cleaned_data['environment_name']
            post.actions_number = form.cleaned_data['actions_number']
            post.content = form.cleaned_data['content']
            post.gif_url = form.cleaned_data['gif_url']
            post.save()
            return HttpResponseRedirect(
                reverse('environments:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'title': post.title,
                'environment_name': post.environment_name,
                'actions_number': post.actions_number,
                'content': post.content,
                'gif_url': post.gif_url
            })

    context = {'post': post, 'form': form}
    return render(request, 'environments/update.html', context)

def delete_environment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('environments:index'))

    context = {'post': post}
    return render(request, 'environments/delete.html', context)