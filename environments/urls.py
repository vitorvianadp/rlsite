from django.urls import path

from . import views

app_name = 'environments'
urlpatterns = [
    path('', views.list_environment_posts, name='index'),
    path('search/', views.search_environment_posts, name='search'),
    path('create/', views.create_environment_post, name='create'),
    path('update/<int:post_id>/', views.update_environment_post, name='update'),
    path('delete/<int:post_id>/', views.delete_environment_post, name='delete'),
    path('<int:post_id>/', views.detail_environment_post, name='detail'),
]