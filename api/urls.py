from django.urls import path
from . import views

urlpatterns = [
    path('chapters/', views.get_chapters, name='get-chapters'),
    path('create-chapter/', views.create_chapter, name='create-chapter'),
]
