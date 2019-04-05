from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^project/', views.project, name='project'),
    url(r'^view_project/(\d+)', views.view_Project, name='view_project'),
    url(r'^myProfile/(\d+)', views.myProfile, name='myProfile'),
    url(r'^search_results/', views.search_results, name='search_results'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)