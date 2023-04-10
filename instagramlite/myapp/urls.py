from django.urls import path, include
from rest_framework.routers import DefaultRouter
from instagramlite.myapp import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSets)
router.register('feed', views.UserProfileFeedViewSets)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
