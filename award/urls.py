from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectCreateView,ProjectListView,ProjectDetailView,UserProjectListView
# ImageListView,ImageDetailView,UserImageListView,ImageUpdateView,ImageDeleteView,CommentCreateView


urlpatterns=[
    # url(r'^$', views.welcome, name = 'award-home'),
    url(r'^$', ProjectListView.as_view(), name = 'award-home'),
    url(r'^project/new/$',ProjectCreateView.as_view(), name='project-create'),
    url(r'^user/(?P<username>\w+)/$', UserProjectListView.as_view(), name='user-projects'),
    url(r'^project/(?P<pk>\d+)/',ProjectDetailView.as_view(), name='project-detail'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)