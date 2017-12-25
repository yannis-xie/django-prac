from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article-column', views.article_column, namespace = 'article_column'),
]