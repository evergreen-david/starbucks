from django.urls import path
from .views      import (
    ProductView,
    ProductPrefetchView
)

urlpatterns = [
    path('/<int:category_id>', ProductView.as_view()),
    path('/prefetch/<int:category_id>', ProductPrefetchView.as_view()),

]

