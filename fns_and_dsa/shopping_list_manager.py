shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")

def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Shopping list is empty.")
def clear_list():
    shopping_list.clear()
    print("Cleared the shopping list.")

def main():
    while True:
        display_menu()
        
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()