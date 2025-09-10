from django.test import TestCase
from ecommerce.models import Product

class ProductModelTest(TestCase):
    def test_product_str_and_price(self):
        p = Product.objects.create(name="TestProduct", price=9.99)
        self.assertEqual(str(p), "TestProduct")
        self.assertAlmostEqual(float(p.price), 9.99, places=2)
