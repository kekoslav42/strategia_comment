from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
