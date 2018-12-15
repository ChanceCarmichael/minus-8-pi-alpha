from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('kdp/', include('kdp.urls')),
	path('admin/', admin.site.urls),
]
