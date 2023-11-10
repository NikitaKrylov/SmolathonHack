from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from smolathon import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('accounts/', include('account.urls')),
    path('', include('social_django.urls'), name='social'),

]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
