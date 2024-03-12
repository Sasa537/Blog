from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('article/', views.ArticlesList.as_view()),
    path('article/<int:pk>', views.ArticlesDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
