from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    #url(r'^$', 'dj_rec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
