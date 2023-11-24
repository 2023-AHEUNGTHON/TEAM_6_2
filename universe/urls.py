
from django.urls import path, include
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    
        openapi.Info(
            title="universe",
            default_version='v1',
            description="API 문서",
            terms_of_service="https://www.google.com/policies/terms/",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('', main, name='main'),
    path('board/<str:category>/', board, name='board'),
    path('post/<str:category>/',post, name='post'),
    path('comment_page/',comment_page,name='comment_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]