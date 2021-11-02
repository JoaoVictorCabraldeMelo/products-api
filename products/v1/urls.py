from django.conf.urls import url
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', ProductsApiView.as_view()),
    path('<int:product_id>', ProductEditDeleteApiView.as_view())
]

