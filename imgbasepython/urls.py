from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import RedirectView

api_urls = [
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^media$', RedirectView.as_view(url = '/media/')),
    url(r'^media/', include('media.urls', namespace='media'))
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api-token-auth/', obtain_jwt_token),

]
