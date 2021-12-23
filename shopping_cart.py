from product import Product

class ShoppingCart:
  def __init__(self) -> None:
    self.products: list[Product] = []
  
  def calculate_total(self):
    total = 0
    for product in self.products:
      total += product.price
    return total
  
  def add_item(self, item: Product):
    self.products.append(item)
    print(f'{item.name} has been added to your cart!')
  
  def empty_cart(self):
    self.products = []
    print('Your cart is now empty.')