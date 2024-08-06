from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zlauth/', include('zlauth.urls')),
    path('blog/', include('blog.urls')),

]
