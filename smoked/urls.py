from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns(
    'smoked.views',
    url('^results$', 'smoked_results', name='results')
)
