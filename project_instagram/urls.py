"""
URL configuration for project_instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include ,re_path
from django.conf import settings
from django.conf.urls.static import static
# from chat_app import routing

urlpatterns = [
    # re_path(r'^', include(routing)),
    path('', include('django_prometheus.urls')),

    path('admin/', admin.site.urls),
    path('', include('user_app.urls')),
    path('follow_user/', include('follow_user.urls')),
    path('chat_app/', include('chat_app.urls')),
    path('post_app/', include('post_app.urls')),
    path('chatting_app/', include('chatting_app.urls')),
    path('api/', include('follow_user.follow_user_api.urls')),
    path('api_post/', include('post_app.post_api.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

