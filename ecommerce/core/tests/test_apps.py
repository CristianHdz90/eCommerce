from django.apps import apps
from django.test import TestCase


class CoreAppTests(TestCase):
    def test_app_is_intalled(self):
        self.assertTrue(apps.is_installed("ecommerce.core"))
