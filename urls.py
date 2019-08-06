"""Ayesha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Device/',views.laptop,name='my_laptop'),
    path('login/',views.my_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('logout/',views.my_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('desktop/',views.desktop,name='my_desktop'),
    path('mobile/',views.mobile,name='my_mobile'),
    path('lap_edit/<int:id>',views.lap_edit,name='lap_edit'),
    path('mob_edit/<int:id>',views.mob_edit,name='mob_edit'),
    path('dek_edit/<int:id>',views.dek_edit,name='dek_edit'),
    path('delete/<int:id>',views.del_dek,name='del_dek'),
    path('mdelete/<int:id>',views.del_mobl,name='del_mobl'),
    path('ldelete/<int:id>',views.del_lap,name='del_lap'),
    path('about/',views.about,name='about_us'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
