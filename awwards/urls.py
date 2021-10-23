from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.display_index,name="index"),
    url('profile/',views.profile, name='profile'),
    url('search/', views.search, name='search'),
    url('project_info/(?P<id>\d+)', views.view_project, name='viewproject'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)