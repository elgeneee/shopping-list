shopping_list = []

def show_help():
  print("What to pick up at the store?")
  print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for help.
Enter 'SHOW' to see current list.
  """)

def show_list():
  print("Here's your list:")
  for item in shopping_list:
    print(item)

def add_to_list():
  shopping_list.append(new_item)
  print('Added {}. {} items total'.format(new_item, len(shopping_list)))

show_help()

while True:
  new_item = input("==> ")
  if new_item.lower() == 'done':
    show_list()
    break
  elif new_item.lower() == 'help':
    show_help()
    continue
  elif new_item.lower() == 'show':
      show_list()
      continue
  add_to_list() 
