from django.conf.urls import url


from . import views

app_name = 'test'
urlpatterns = [
    url(r'^$', views.current_datetime, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^myview/$', views.myview, name='myview'),
    url(r'^yourname/$', views.get_name, name='your-name'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'articles/$', views.manage_articles, name='articles'),
]