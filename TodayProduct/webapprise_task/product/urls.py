from django.urls import path
from .views import product_list,add_product,update_product,delete_product,product_detail,generate_invoice
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', product_list, name='product-list'),
    path('add/', add_product, name='add_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('invoice/<int:pk>/', generate_invoice, name='generate_invoice'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
