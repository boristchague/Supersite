
from django.contrib import admin
from django.urls import path
from ColisVip import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil', views.home),
]

urlpatterns += staticfiles_urlpatterns()