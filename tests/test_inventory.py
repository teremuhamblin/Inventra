from django.test import TestCase
from inventory.models import Category, Part, StockItem


class InventoryModelTests(TestCase):
    def test_create_category(self):
        cat = Category.objects.create(name="TestCat")
        self.assertEqual(str(cat), "TestCat")
