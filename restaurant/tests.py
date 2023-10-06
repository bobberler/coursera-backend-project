from django.test import TestCase
from .models import Menu
from .serializers import menuSerializer

# Create your tests here.


class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Soda", price=0, inventory=0)

    def test_get_menu(self):
        icecream = Menu.objects.get(title="IceCream")
        self.assertEqual(icecream.title, "IceCream")
        self.assertEqual(icecream.price, 80)
        self.assertEqual(icecream.inventory, 100)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_item = menuSerializer(data=items, many=True)
        serialized_item.is_valid()