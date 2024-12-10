def add_item(inventory, item_name, quantity, price):
    """
    Add a new item to the inventory or update the quantity and price of an existing item.

    :param inventory: The inventory dictionary that stores all items.
                       Structure: {item_name: {'quantity': int, 'price': float}}
    :param item_name: The name of the item to add (string).
    :param quantity: The number of items to add (integer).
    :param price: The price of the item (float).
    :return: None
    """
    # Check if the item already exists in the inventory
    if item_name in inventory:
        # If the item exists, increase its quantity and update the price
        inventory[item_name]['quantity'] += quantity
        inventory[item_name]['price'] = price
        print(f"Updated {item_name}: Quantity: {inventory[item_name]['quantity']}, Price: {price:.2f}")
    else:
        # If the item does not exist, add it as a new entry in the inventory
        inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added new item: {item_name} - Quantity: {quantity}, Price: {price:.2f}")


def remove_item(inventory, item_name, quantity):
    """
    Remove a specified quantity of an item from the inventory.

    :param inventory: The inventory dictionary that stores all items.
    :param item_name: The name of the item to remove (string).
    :param quantity: The number of items to remove (integer).
    :return: None
    """
    # Check if the item exists in the inventory
    if item_name in inventory:
        # Check if there is enough quantity to remove
        if inventory[item_name]['quantity'] >= quantity:
            # Reduce the quantity of the item
            inventory[item_name]['quantity'] -= quantity
            print(f"Removed {quantity} of {item_name}. Remaining: {inventory[item_name]['quantity']}")

            # If the quantity becomes 0, remove the item completely from the inventory
            if inventory[item_name]['quantity'] == 0:
                del inventory[item_name]
                print(f"{item_name} is now out of stock and removed from inventory.")
        else:
            # If there is not enough quantity to remove, show an error message
            # CHANGED: Raise ValueError instead of printing
            raise ValueError(f"Not enough quantity to remove for {item_name}.")
    else:
        # If the item does not exist in the inventory, show an error message
        # CHANGED: Raise KeyError instead of printing
        raise KeyError(f"{item_name} does not exist in the inventory.")


def update_item_price(inventory, item_name, new_price):
    """
    Update the price of an existing item in the inventory.

    :param inventory: The inventory dictionary that stores all items.
    :param item_name: The name of the item whose price needs to be updated (string).
    :param new_price: The new price of the item (float).
    :return: None
    """
    # Check if the item exists in the inventory
    if item_name in inventory:
        # Update the price of the item
        inventory[item_name]['price'] = new_price
        print(f"Updated price of {item_name} to {new_price:.2f}")
    else:
        # If the item does not exist, show an error message
        # CHANGED: Raise KeyError instead of printing
        raise KeyError(f"{item_name} does not exist in the inventory.")


def view_inventory(inventory):
    """
    Display the current inventory with item names, quantities, and prices.

    :param inventory: The inventory dictionary that stores all items.
    :return: None
    """
    # Check if the inventory is empty
    if not inventory:
        print("The inventory is empty.")
    else:
        # Display all items in the inventory
        print("\n----- Current Inventory -----")
        for item_name, details in inventory.items():
            print(f"{item_name}: Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
        print("-----------------------------")


def search_item(inventory, item_name):
    """
    Search for an item in the inventory and display its details.

    :param inventory: The inventory dictionary that stores all items.
    :param item_name: The name of the item to search for (string).
    :return: None
    """
    # Check if the item exists in the inventory
    if item_name in inventory:
        # Display the item's details
        details = inventory[item_name]
        print(f"{item_name}: Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
        # CHANGED: Return the item's details
        return details
    else:
        # If the item does not exist, show an error message
        # CHANGED: Raise KeyError instead of printing
        raise KeyError(f"{item_name} does not exist in the inventory.")


def main():
    """
    Main function to demonstrate the inventory system.
    Initializes the inventory and performs various operations.
    """
    # Step 1: Initialize an empty dictionary to represent the inventory
    inventory = {}

    # Step 2: Add items to the inventory
    # Adding apples, bananas, and oranges with their respective quantities and prices
    add_item(inventory, "apple", 50, 0.5)
    add_item(inventory, "banana", 30, 0.2)
    add_item(inventory, "orange", 20, 0.8)

    # Step 3: View the current inventory
    # This will display all the items currently in the inventory
    view_inventory(inventory)

    # Step 4: Update the price of an existing item
    # Changing the price of bananas to 0.25
    update_item_price(inventory, "banana", 0.25)

    # Step 5: Remove a specific quantity of an item
    # Removing 10 apples from the inventory
    remove_item(inventory, "apple", 10)
    try:
        # Trying to remove more oranges than are available
        remove_item(inventory, "orange", 25)
    except ValueError as e:
        print(e)  # CHANGED: Added exception handling for demonstration

    # Step 6: Search for specific items in the inventory
    # Searching for an existing item (apple)
    search_item(inventory, "apple")
    try:
        # Searching for a non-existent item (grape)
        search_item(inventory, "grape")
    except KeyError as e:
        print(e)  # CHANGED: Added exception handling for demonstration

    # Step 7: View the updated inventory
    # This will show the inventory after all operations are performed
    view_inventory(inventory)


# Entry point of the program
if __name__ == "__main__":
    main()
