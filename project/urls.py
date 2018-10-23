from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #path('', TemplateView.as_view(template_name='club-home.html'), name='club-home'),
    path('', include('zibcrm.urls')),
    url(r'^health$', health),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
