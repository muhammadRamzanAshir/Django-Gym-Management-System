from django.urls import path,include
from django.conf.urls.static import static
from fifth import settings
from . import views  # Adjust based on your project structure
import accounts

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
