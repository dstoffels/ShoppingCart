def validate_int_input(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = 'Please enter a number'