from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('customer.urls', namespace='customer')),
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls', namespace='customer')),
]
