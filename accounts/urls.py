from django.urls import path
from django.conf.urls.static import static
from fifth import settings
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.Auth_view, name='auth'),
    # path('signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
