from django.urls import path
from apps.wiki import views

urlpatterns = [
    path("", views.wiki_page_view),
]
