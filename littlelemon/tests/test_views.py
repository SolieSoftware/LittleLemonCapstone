from django.test import TestCase
from restaurant.models import Booking, Menu

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.item_1 = Menu.objects.create(title="Bolognaise", price=10.50, inventory=12)
        self.item_2 = Menu.objects.create(title="Pesto", price=8.50, inventory=8)
        self.item_3 = Menu.objects.create(title="Pomodoro", price=9.00, inventory=5)
        
    def test_getall(self) -> None:
        items = Menu.objects.all()
        self.assertEqual(items.count(), 3)
        self.assertIn(self.item_1, items)
        self.assertEqual(self.item_1.title, "Bolognaise")
        self.assertIn(self.item_2, items)
        self.assertEqual(self.item_2.price, 8.50)
        self.assertIn(self.item_3, items)
        self.assertEqual(self.item_3.inventory, 5)
        
