from rest_framework import routers
from .views import BookViewSets


router = routers.DefaultRouter(trailing_slash = False)
router.register('books', BookViewSets)
