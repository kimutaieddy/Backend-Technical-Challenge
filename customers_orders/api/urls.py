from django.urls import path, include  
from rest_framework.routers import SimpleRouter  
from .views import CustomerViewSet, OrderViewSet 


# Initialize SimpleRouter instance
router = SimpleRouter()
router.register(r'customers', CustomerViewSet)  
router.register(r'orders', OrderViewSet)  


urlpatterns = [
    path('api/v1/', include(router.urls)), 
    path('oidc/', include('mozilla_django_oidc.urls')), 
]
