from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

class DocsView(APIView):
    """
    RESTFul Documentation of my app
    """
    def get(self, request, *args, **kwargs):
        apidocs = {'Api-root': request.build_absolute_uri('api'),
                   }
        return Response(apidocs)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('app.api.urls')),
    path('', DocsView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
