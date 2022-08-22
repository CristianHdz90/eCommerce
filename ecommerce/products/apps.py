from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsApp(AppConfig):
    name = "ecommerce.products"
    verbose_name = _("products")
