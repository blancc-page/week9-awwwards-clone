from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('users', views.UserViewSet)
# router.register('posts', views.PostViewSet)
# router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('project/', views.project, name='project'),
    path('search/', views.search_project, name='search'),
]