from django.conf.urls import include, url
from django.contrib import admin
from core.views import home, add_task

urlpatterns = [
	url(r'^add_task/$', add_task, name='add_task'),
	url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

]
