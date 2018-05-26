"""hellowebapp URL Configuration

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
from collection import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.post_detail, name="post_detail"),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^admin/', admin.site.urls),
]
