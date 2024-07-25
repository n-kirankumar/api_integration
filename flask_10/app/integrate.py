import requests
import json

BASE_URL = 'http://localhost:5000'

def get_items():
    response = requests.get(f'{BASE_URL}/items')
    print(response.json())

def add_item(item_id, item_name):
    response = requests.post(f'{BASE_URL}/items', json={"id": item_id, "name": item_name})
    print(response.json())

def update_item(item_id, item_name):
    response = requests.patch(f'{BASE_URL}/items/{item_id}', json={"name": item_name})
    print(response.json())

def delete_item(item_id):
    response = requests.delete(f'{BASE_URL}/items/{item_id}')
    print(response.json())

def main():
    while True:
        print("\nOptions:")
        print("1. Get Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            get_items()
        elif choice == '2':
            item_id = input("Enter item ID: ")
            item_name = input("Enter item name: ")
            add_item(item_id, item_name)
        elif choice == '3':
            item_id = input("Enter item ID: ")
            item_name = input("Enter new item name: ")
            update_item(item_id, item_name)
        elif choice == '4':
            item_id = input("Enter item ID: ")
            delete_item(item_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
