from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
  def test_main_url_is_exist(self):
    response = Client().get('/main/')
    self.assertEqual(response.status_code, 200)

  def test_main_using_main_template(self):
    response = Client().get('/main/')
    self.assertTemplateUsed(response, 'main.html')

  def test_create_object(self):
    Item.objects.create(name='Cheese Sauce', amount=127, description='A product made of sauce')
    Cheese_Sauce = Item.objects.get(name='Cheese Sauce')
    self.assertEqual(Cheese_Sauce.name, 'Cheese Sauce')
    self.assertEqual(Cheese_Sauce.amount, 127)
    self.assertEqual(Cheese_Sauce.description, 'A product made of sauce')
