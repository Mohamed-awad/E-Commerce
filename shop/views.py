from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if category_slug:
    category = get_object_or_404(Category, slug= category_slug)
    products = Product.objects.filter(category= category)

  context = {
    'category': category,
    'categories': categories,
    'products': products
  }

  return render(request, 'shop/products/list.html', context)


def product_detail(request, id, slug):
  product = get_object_or_404(Product, id=id, slug=slug, available= True)
  cart_product_form = CartAddProductForm()
  context = {

    'product': product,
    'cart_product_form':cart_product_form,
  }

  return render(request, 'shop/products/detail.html', context)