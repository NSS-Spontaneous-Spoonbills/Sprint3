from django.conf.urls import url
from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.Product_Home_List_View, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    # url(r'^sell$', views.sell_product, name='sell'),
    # url(r'^products$', views.list_products, name='list_products'),
    path('product/<pk>/', views.Product_Detail_View, name="product_detail"),
    url(r'^product_types$', views.Product_Type_List_View, name='product_types'),
    url(r'^product_category$', views.Product_Category_View, name='product_category'),
]
