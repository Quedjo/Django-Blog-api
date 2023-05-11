from django.urls import path
from .views import postslist,postsdetail

urlpatterns=[
path("",postslist.as_view(),name="postlist"),
path("<int:pk>/",postsdetail.as_view(),name="postdetail"),
]