from django.conf.urls import url


from . import views

app_name = 'semantic_web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chart/$', views.chart, name='chart'),
]