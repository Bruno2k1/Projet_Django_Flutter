"""
URL configuration for BlogAFN_2k24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from BlogAFN import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Articles API")
router = routers.DefaultRouter()
router.register(r'BlogAFN', views.ArticleViewSet,basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include the router's URL patterns for the BlogAFN app
    path('BlogAFN/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'),
    path('api/docs/', schema_view),
]


