from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.index, name='blog_index'),
	url(r'^blog/$', views.index),
	url(r'^blog/(?P<kind>[a-z]+)/$', views.article, name='blog_list'),
	url(r'^blog/searchbytag/(?P<tag>[a-zA-Z0-9_+#*\u4e00-\u9fa5]+)/$', views.article, name='blog_search_by_tag'),
	url(r'^blog/searchbykey/$', views.article, name='blog_search_by_key'),
	url(r'^blog/(?P<kind>[a-z]{4})/(?P<blog_id>[0-9]+)/$', views.blog, name='blog_page'),
	url(r'^blog/(?P<kind>[a-z]{4})/(?P<blog_id>[0-9]+)/comment/$', views.comment, name='blog_comment'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)