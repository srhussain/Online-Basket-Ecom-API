from django.urls import path
from api.views import product_views as views



urlpatterns = [
    path('',views.getproducts,name='products'),
    path('create/',views.createProduct,name='create-products'),
    path('upload/',views.uploadImage,name='image-upload'),
    path('<str:pk>/reviews/',views.createProductReview,name='create_review'),
    path('top/',views.getTopProducts,name='top-products'),
    path('<str:pk>/',views.getproduct,name='products'),
    path('update/<str:pk>/',views.updateProduct,name='update-products'),
    path('delete/<str:pk>/',views.deleteProduct,name='delete-products'),
]
