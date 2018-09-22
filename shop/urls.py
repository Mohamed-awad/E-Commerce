from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
  url('^$', views.product_list, name='product_list'),
  url(r'^add_product/$', views.AddProduct.as_view(), name='add_product'),
  url('^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
  url(r'^api/category/$', views.CategoryList.as_view(), name='list_category_api'),
  url(r'^api/category/(?P<category_slug>[-\w]+)/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='detail_category_api'),
  url(r'^api/product/$', views.ProductList.as_view(), name='list_product_api'),
  url(r'^api/product/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail.as_view(), name='detail_product_api'),
]
