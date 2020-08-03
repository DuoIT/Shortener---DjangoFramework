"""url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shorty.views import shortyReditectClassReView, homeView
#shorty_re_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', homeView.as_view()),
    # url(r'^a/(?P<shortcode>[\w-]+)/$', shorty_re_view),
    url(r'^(?P<shortcode>[\w-]+)/$', shortyReditectClassReView.as_view(), name='scode')
]
