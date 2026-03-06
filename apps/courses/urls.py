from django.urls import path
from apps.courses import views


urlpatterns = [path("courses/", views.index, name="home")]
