from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
  url(r'^create/$', views.order_create, name='order_create'),
  url(r'^$', views.OrderList.as_view(), name='list_orders_api'),
  url(r'^(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='detail_order_api'),
  url(r'^order_item/$', views.OrderItemList.as_view(), name='list_order_item_api'),
  url(r'^order_item/(?P<pk>[0-9]+)/$', views.OrderItemDetail.as_view(), name='detail_order_item_api'),

]

