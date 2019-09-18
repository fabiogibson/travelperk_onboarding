from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from recipes.router import router as recipe_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(recipe_router.urls))
]
