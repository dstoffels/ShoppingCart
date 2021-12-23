from product import Product
from shopping_cart import ShoppingCart

class Customer:
  def __init__(self, name) -> None:
      self.name = name
      self.cart = ShoppingCart()

  def add_item_to_cart(self, item: Product):
    self.cart.add_item(item)
  
  def view_cart(self):
    print('Your Cart:')
    for item in self.cart.products:
      print(item.name)