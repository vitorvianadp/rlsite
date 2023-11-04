from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post

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
        post_title = request.POST['title']
        environment_name = request.POST['environment_name']
        actions_number = request.POST['actions_number']
        content = request.POST['content']
        #creation_date = request.POST['creation_date']
        gif_url = request.POST['gif_url']
        post = Post(title=post_title,
                      environment_name=environment_name,
                      actions_number=actions_number,
                      content=content,
                      #creation_date=creation_date,
                      gif_url=gif_url)
        post.save()
        return HttpResponseRedirect(
            reverse('environments:detail', args=(post.id, )))
    else:
        return render(request, 'environments/create.html', {})
    
def update_environment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.environment_name = request.POST['environment_name']
        post.actions_number = request.POST['actions_number']
        post.content = request.POST['content']
        post.gif_url = request.POST['gif_url']
        post.save()
        return HttpResponseRedirect(
            reverse('environments:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'environments/update.html', context)


def delete_environment_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('environments:index'))

    context = {'post': post}
    return render(request, 'environments/delete.html', context)