from django.conf.urls import url


from . import views

app_name = 'pure_layout_blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]