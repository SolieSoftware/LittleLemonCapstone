from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItem.as_view()),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('api-token-auth/', obtain_auth_token),
]