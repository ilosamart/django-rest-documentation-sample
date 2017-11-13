from rest_framework import routers
from .views import UserViewSet, SnippetViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'snippet', SnippetViewSet)
