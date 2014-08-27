from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'demoapp.views.home', name='home'),
    url(r'^add/', 'demoapp.views.add', name='add'),

)
