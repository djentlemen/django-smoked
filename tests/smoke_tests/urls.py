from django.conf.urls import include, url

urlpatterns = [
    url('^_smoked', include('smoked.urls', namespace='smoked')),
]