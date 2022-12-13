from django.contrib import admin
from django.urls import path, include
from Todo_list.urls import router
from Todo_list import views


urlpatterns = [
    # admin page
    path('admin/', admin.site.urls),

    # homepage
    path('', views.index, name="index"),
    # Including all URLs from router urls
    path('todo/', include(router.urls), name="api"),

    # authentication
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
]
