from django.conf.urls import patterns, url

from .views import AAAAFeedView


urlpatterns = patterns(
    '',
    url(r'^feed/$', view=AAAAFeedView.as_view()),
)
