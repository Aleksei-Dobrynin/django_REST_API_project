from django.urls import path
from .views import *
urlpatterns = [
    path('',StoreAPI.as_view()),
    path('product/',ProductAPI.as_view()),
    path('<int:pk>/', StoreDetailAPI.as_view()),
    path('<int:pk>/add/',StoreAddAPI),
    path('<int:pk>/buy/',StoreBuyAPI),
]
