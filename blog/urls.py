# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),  # 主页，通常不需要前缀
    path('detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # 博客详情页面
    path('pub/', views.pub_blog, name='pub_blog'),  # 发布博客页面
    path('comment/pub',views.pub_comment,name='pub_comment')
    ,path('search',views.search,name='search'),
]
