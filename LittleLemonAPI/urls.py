from django.urls import path , include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'booking', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [

    path('api-token-auth/', obtain_auth_token),
    path("menu-items/", views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
    path('message/', views.msg),
]
