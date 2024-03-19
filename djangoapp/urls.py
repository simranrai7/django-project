
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('',views.base, name="base"),
    path('post/', views.post, name="post"),
    path('detail/<int:pk>', views.detail, name='detail'),
    path("gallery/", views.gallery, name="gallery"),
]