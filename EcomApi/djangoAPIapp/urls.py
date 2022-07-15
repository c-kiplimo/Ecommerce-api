from django.urls import path
from .views import *

urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>', DetailsCategory.as_view(),name='singlecategory'),
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>', DetailsBook.as_view(),name='singlebook'),
    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>', DetailsProduct.as_view(),name='singleproduct'),

]
