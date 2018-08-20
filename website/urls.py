from django.conf.urls import url
from . import views
from .views import Product_Type_View
from .views import *

# from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    # url(r'^sell$', views.sell_product, name='sell'),
    # url(r'^products$', views.list_products, name='list_products'),
    url(r'^product_types$', views.Product_Type_View, name='product_type_list'),
]
