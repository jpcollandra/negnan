from django.urls import path
from.views import (PostListView,
 PostDetailView,
 PostCreateView,
 PostUpdateView,
 PostDeleteView,
 UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='docs-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='docs-about'),
    path('download', views.download, name='docs-download'),
    path('download_here', views.download_here, name='docs-download_here'),
    path('privacy', views.privacy, name='docs-privacy'),
    path('terms', views.terms, name='docs-terms'),
    path('view_404', views.view_404, name='docs-view_404')

]
