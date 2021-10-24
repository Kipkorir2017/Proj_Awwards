from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^$',views.display_index,name="index"),
    url('profile/',views.profile, name='profile'),
    url('search/', views.search, name='search'),
    url('signup/',views.signup,name="sign_up"),
    url('project_info/(?P<id>\d+)', views.view_project, name='viewproject'),
    url('upload/',views.post_project,name='post_proj'),
    url('update/',views.update_profile, name='update_prof'),

     #api endpoints
    url('api/v1/profile',views.ProfileList.as_view(),name='profileEndpoint'),
    url('api/v1/projects',views.ProjectList.as_view(),name='projectsEndpoint')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)