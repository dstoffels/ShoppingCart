from customer import Customer
from helpers import validate_int_input

MENU = f'''
1) New Product
2) View Cart
3) Clear Cart
4) Exit

Select an option: '''

customer = Customer()

while True:
  print(f'\nCustomer: {customer.name}')
  user_input = validate_int_input(MENU)

  match user_input:
    case 1:
      customer.add_new_item_to_cart()
    case 2:
      customer.view_cart()
    case 3:
      customer.cart.empty_cart()
    case 4:
      exit()