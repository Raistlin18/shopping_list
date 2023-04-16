'''
    This is a shopping list app.
'''

shop_list = []

def show_help():
    print("What should we pick up at the store?")
    print('\nMenu:\nDONE - to stop adding items\nHELP - to show this menu\nSHOW - to show the current list\nREMOVE - to remove an item from the list\nCLEAR - to clear the list\n')


def show_list():
    print("Here's your list:\n")
    for item in shop_list:
        print(item)

def add_to_list(new_item):
    shop_list.append(new_item)
    print("Added! List has {} items.\n".format(len(shop_list)))
    show_list()

def remove_from_list(item):
    shop_list.remove(item)
    print("Removed! List has {} items.\n".format(len(shop_list)))
    show_list()

def clear_list():
    shop_list.clear()
    print("Cleared! List has {} items.\n".format(len(shop_list)))
    show_list()

def main():
    show_help()
    while True:
        new_item = input(">>> ")

        if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
            break
        elif new_item.upper() == "HELP":
            show_help()
            continue
        elif new_item.upper() == "SHOW":
            show_list()
            continue
        elif new_item.upper() == "REMOVE":
            item = input("What would you like to remove? ")
            remove_from_list(item)
            continue
        elif new_item.upper() == "CLEAR":
            clear_list()
            continue
        add_to_list(new_item)

    show_list()

main()
