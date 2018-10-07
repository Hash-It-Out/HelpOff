"""HelpOff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home_page,contact,login_user,signup_user,logout_user,index
from Motivate.views import chat,fun,motivate,contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index),
	url(r'^login/$', login_user, name="login"),
    url(r'^signup/$', signup_user, name="signup"),
    url(r'^home/$', home_page, name="home"),
    url(r'^logout/$', logout_user, name="logout"),
	url(r'^chat$', chat, name="chat"),
	url(r'^fun$', fun, name="fun"),
	url(r'^motivate$', motivate, name="motivate"),
    url(r'^contact/$',contact_us)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
