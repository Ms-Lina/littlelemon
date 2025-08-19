from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView
class MenuViewTest(TestCase):
    def setup():
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        item.save()
        item = Menu.objects.create(Title="Pickles", Price=8, Inventory=100)
        item.save()
        item = Menu.objects.create(Title="Cheese", Price=8, Inventory=100)
        item.save()
    def test_getall():
        #MenuItemView()
        #Need to put test in?
        return True