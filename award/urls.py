from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectCreateView
# ImageListView,ImageDetailView,UserImageListView,ImageUpdateView,ImageDeleteView,CommentCreateView


urlpatterns=[
    url(r'^$', views.welcome, name = 'award-home'),
    url(r'^project/new/$',ProjectCreateView.as_view(), name='project-create'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)