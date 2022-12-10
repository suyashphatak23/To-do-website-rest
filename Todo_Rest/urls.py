from django.contrib import admin
from django.urls import path, include
from Todo_list.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),

    # Including all URLs from router urls
    path('todo/', include(router.urls)),
]
