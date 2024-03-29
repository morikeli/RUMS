from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Administrator Panel'
admin.site.site_title = 'School MS'
admin.site.index_title = 'Karibu tena ...'

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

