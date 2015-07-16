from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^movies/$', views.MoviesList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MoviesDetail.as_view()),
    url(r'^$', views.signup),
    url(r'^add_movie', views.add_movie),
    url(r'^add_genre', views.add_genre),
    url(r'^list$', views.movie_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)