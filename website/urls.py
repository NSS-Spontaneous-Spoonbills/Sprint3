from django.conf.urls import url
from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.Product_Home_List_View, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    path('payment_types/', views.payment_list_view, name='payment_list'),
    url(r'^accounthome', views.my_account_home, name='account_home'),
    # url(r'^sell$', views.sell_product, name='sell'),
    # url(r'^products$', views.list_products, name='list_products'),
    path('product/<pk>/', views.Product_Detail_View, name="product_detail"),
    url(r'^product_types$', views.Product_Type_List_View, name='product_types'),
    path('product_category/<pk>/', views.product_category_view, name='product_category'),
    path('order_history', views.order_history, name='order_history'),
]
