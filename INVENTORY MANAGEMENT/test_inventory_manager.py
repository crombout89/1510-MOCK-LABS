import unittest
from inventory_manager import *

class TestInventorySystem(unittest.TestCase):
    """
    Unit test suite for the inventory system.
    """

    def setUp(self):
        """
        Set up a fresh inventory dictionary for each test.
        """
        self.inventory = {}

    def test_add_item_new(self):
        """
        Test adding a new item to the inventory.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        self.assertIn("apple", self.inventory)
        self.assertEqual(self.inventory["apple"]["quantity"], 10)
        self.assertEqual(self.inventory["apple"]["price"], 0.5)

    def test_add_item_existing(self):
        """
        Test adding more quantity to an existing item and updating its price.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        add_item(self.inventory, "apple", 5, 0.6)  # Adding 5 more apples, updating price
        self.assertEqual(self.inventory["apple"]["quantity"], 15)
        self.assertEqual(self.inventory["apple"]["price"], 0.6)

    def test_remove_item_existing(self):
        """
        Test removing a quantity from an existing item.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        remove_item(self.inventory, "apple", 5)
        self.assertEqual(self.inventory["apple"]["quantity"], 5)

    def test_remove_item_entire_stock(self):
        """
        Test removing all quantity of an existing item (item should be removed from inventory).
        """
        add_item(self.inventory, "apple", 10, 0.5)
        remove_item(self.inventory, "apple", 10)  # Remove all apples
        self.assertNotIn("apple", self.inventory)

    def test_remove_item_insufficient_quantity(self):
        """
        Test attempting to remove more quantity than available (should raise ValueError).
        """
        add_item(self.inventory, "apple", 5, 0.5)
        with self.assertRaises(ValueError):
            remove_item(self.inventory, "apple", 10)

    def test_remove_item_nonexistent(self):
        """
        Test attempting to remove an item that does not exist in the inventory (should raise KeyError).
        """
        with self.assertRaises(KeyError):
            remove_item(self.inventory, "banana", 5)

    def test_update_item_price_existing(self):
        """
        Test updating the price of an existing item.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        update_item_price(self.inventory, "apple", 0.6)
        self.assertEqual(self.inventory["apple"]["price"], 0.6)

    def test_update_item_price_nonexistent(self):
        """
        Test updating the price of a non-existent item (should raise KeyError).
        """
        with self.assertRaises(KeyError):
            update_item_price(self.inventory, "banana", 0.6)

    def test_search_item_existing(self):
        """
        Test searching for an existing item.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        result = search_item(self.inventory, "apple")
        self.assertEqual(result["quantity"], 10)
        self.assertEqual(result["price"], 0.5)

    def test_search_item_nonexistent(self):
        """
        Test searching for a non-existent item (should raise KeyError).
        """
        with self.assertRaises(KeyError):
            search_item(self.inventory, "banana")

    def test_view_inventory_empty(self):
        """
        Test viewing an empty inventory (should simply check the dictionary is empty).
        """
        self.assertEqual(len(self.inventory), 0)

    def test_view_inventory_with_items(self):
        """
        Test viewing a populated inventory.
        """
        add_item(self.inventory, "apple", 10, 0.5)
        add_item(self.inventory, "banana", 20, 0.25)
        self.assertEqual(len(self.inventory), 2)
        self.assertIn("apple", self.inventory)
        self.assertIn("banana", self.inventory)

if __name__ == "__main__":
    # Run all the unit tests
    unittest.main()