
from django.contrib import admin
from django.urls import path, include
from waaw import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contest', views.contest, name='contest'),
    path('features', views.plan, name='plan'),
    path('more', views.more, name='more'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
