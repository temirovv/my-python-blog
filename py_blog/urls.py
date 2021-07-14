from django.urls import path
from .views import PyArticlesListView, PyArticlesDetailView


urlpatterns = [
    path('read/<int:pk>/', PyArticlesDetailView,
         name='article_detail'),
    path('', PyArticlesListView.as_view(), name='home'),
]
