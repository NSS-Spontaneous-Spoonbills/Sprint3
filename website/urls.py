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
    path('payment_types/new/', views.payment_new_view, name='payment_new'),
    path('payment_types/<pk>/', views.payment_detail_view, name='payment_detail'),
    path('payment_types/update/<pk>', views.payment_update_view, name='payment_update'),
    url(r'^accounthome', views.my_account_home, name='account_home'),
    url(r'^accountedit/(?P<pk>\d+)/$', views.edit_account_info, name='account_edit'),
    # url(r'^sell$', views.sell_product, name='sell'),
    # url(r'^products$', views.list_products, name='list_products'),
    path('product/<pk>/', views.Product_Detail_View, name="product_detail"),
    url(r'^product_types$', views.Product_Type_List_View, name='product_types'),
    path('product_category/<pk>/', views.product_category_view, name='product_category'),
]
