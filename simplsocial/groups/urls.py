#groups urls.py file 
from django.conf.urls import url
from groups import views

app_name = "groups"

urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    url(r'^new/$',views.CreateGroup.as_view(),name="create"),
    url(r'^posts/in/(?P<slug>[-\W]+)/$',views.Singleroup.as_view(),name="single"),

]
