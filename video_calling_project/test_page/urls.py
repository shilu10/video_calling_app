from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_tst),
    path('s3url/', views.post_url),
    path('videos/', views.videos_page),
    path('take/', views.test_page)

]