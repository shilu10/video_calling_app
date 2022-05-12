from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_page),
    path('s3url/', views.post_url),
    path('videos/', views.videos_page),

]