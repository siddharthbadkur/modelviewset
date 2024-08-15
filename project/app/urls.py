from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', Studentviewset, basename='users')
urlpatterns =[
     path('users',user .as.is_valid())
]
