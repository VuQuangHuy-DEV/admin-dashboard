from django.contrib import admin
from django.urls import path, include

from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),

    path('api/v1/general/', include('general.urls')),
    path('api/v1/booking/', include('booking.urls')),
    path('api/v1/rental/', include('rental.urls')),
    path('api/v1/bidding/', include('bidding.urls')),

    # admin
    path('api/v1/admin/customer/', include('customer_admin.urls')),
    path('api/v1/admin/request/', include('request_admin.urls')),

    path('api/v1/general/', include('general.urls')),
    path('api/v1/booking/', include('booking.urls')),
    path('api/v1/rental/', include('rental.urls')),
    path('api/v1/bidding/', include('bidding.urls')),

    path('api/v1/admin/request/', include('request_admin.urls')),
    path('api/v1/admin/customer/', include('customer_admin.urls')),




]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class CustomAdminSite(admin.AdminSite):
    site_header = 'a'
    site_title = 'b'
    index_title = 'c'


admin.site = CustomAdminSite(name='customadmin')
