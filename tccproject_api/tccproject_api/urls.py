from rest_framework_swagger.views import get_swagger_view
from django.urls.conf import include, re_path

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    re_path(r'^', include('api.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^schema/$', schema_view)
]
