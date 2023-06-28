"""django_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import routers

from sales.views.user_view_set import UserViewSet
from sales.views.invoice_view_set import InvoiceViewSet
from sales.views.cart_view_set import CartViewSet
from stock.views.product_view_set import ProductViewSet
from .views import LogInView
from .views import LogOutView

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'carts', CartViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
]
