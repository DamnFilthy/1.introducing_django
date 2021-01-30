from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view, test


urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('test/', test, name='test'),
    path('admin/', admin.site.urls),
]
