from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
  path('v1/', include('products.v1.urls'))
]