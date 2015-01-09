from django.conf.urls import patterns, include, url
from django.conf.urls import url, include

from django.contrib import admin
from django.views.generic import TemplateView

from authserv import views

admin.autodiscover()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^register/', TemplateView.as_view(template_name='register.html'), name='register'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/create_user/', views.create_user_api, name="create_user_api"),
    url(r'^api/login/', views.login_api, name="login_api"),
    url(r'^api/check_token/', views.check_token, name="check_token"),
    url(r'^api/get_user/(?P<user_name>[^/]+)/$', views.get_user, name="get_user"),
    url(r'^admin/', include(admin.site.urls)),



)
