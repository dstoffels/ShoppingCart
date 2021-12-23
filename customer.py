from helpers import validate_int_input
from product import Product
from shopping_cart import ShoppingCart

class Customer:
  def __init__(self) -> None:
      self.name = input('Please enter your name: ')
      self.cart = ShoppingCart()

  def add_new_item_to_cart(self):
    product_name = input('Enter product name: ')
    product_price = validate_int_input('Enter price: ')
    product_category = input('Enter product category: ')
    product = Product(product_name, product_price, product_category)
    self.cart.add_item(product)
  
  def view_cart(self):
    print('\nYour Cart:\n')
    for item in self.cart.products:
      print(item.name)
    print(f'\nTOTAL: ${self.cart.calculate_total()}\n')
    input('Press enter to continue')