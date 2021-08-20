from django.contrib import admin
from django.urls import path
from . import views
app_name="article"
urlpatterns = [
    path('article/<int:id>',views.detail,name="detail"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('edit/<int:id>/',views.editArticle,name="edit"),
    path('delete/<int:id>/',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>/',views.addComment,name="comment"),
]