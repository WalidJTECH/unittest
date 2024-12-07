"""
Unit tests for the Drink, Food, and Order classes.
"""

import unittest


class Drink:
    """Class to represent a drink with a single base and multiple flavors."""

    _valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    _valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self):
        """Initialize a drink with no base and no flavors."""
        self._base = None
        self._flavors = set()

    def add_base(self, base):
        """Add a valid base to the drink."""
        if base not in self._valid_bases:
            raise ValueError(f"Invalid base: {base}")
        self._base = base

    def get_base(self):
        """Return the base of the drink."""
        return self._base

    def add_flavor(self, flavor):
        """Add a valid flavor to the drink."""
        if flavor not in self._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        if flavor in self._flavors:
            raise ValueError(f"Flavor '{flavor}' has already been added.")
        self._flavors.add(flavor)

    def get_flavors(self):
        """Return the list of flavors added to the drink."""
        return list(self._flavors)


class Food:
    """Class to represent a food item with optional toppings."""

    _valid_food_items = {
        'Hotdog': 2.30,
        'Corndog': 2.00,
        'Ice Cream': 3.00,
        'Onion Rings': 1.75,
        'French Fries': 1.50,
        'Tater Tots': 1.70,
        'Nacho Chips': 1.90
    }
    _valid_toppings = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Nacho Cheese': 0.30,
        'Chili': 0.60,
        'Bacon Bits': 0.30,
        'Ketchup': 0.00,
        'Mustard': 0.00
    }

    def __init__(self, food_item):
        """Initialize a food item with no toppings."""
        if food_item not in self._valid_food_items:
            raise ValueError(f"Invalid food item: {food_item}")
        self._food_item = food_item
        self._base_price = self._valid_food_items[food_item]
        self._toppings = {}

    def add_topping(self, topping):
        """Add a valid topping to the food item."""
        if topping not in self._valid_toppings:
            raise ValueError(f"Invalid topping: {topping}")
        self._toppings[topping] = self._valid_toppings[topping]

    def get_toppings(self):
        """Return the list of toppings added to the food item."""
        return list(self._toppings.keys())

    def get_price(self):
        """Return the total price of the food item, including toppings."""
        return self._base_price + sum(self._toppings.values())


class Order:
    """Class to manage a collection of food and drink items."""

    def __init__(self):
        """Initialize an empty order."""
        self._items = []

    def add_item(self, item):
        """Add a food or drink item to the order."""
        self._items.append(item)

    def remove_item(self, index):
        """Remove an item from the order by its index."""
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index.")
        self._items.pop(index)

    def get_num_items(self):
        """Return the total number of items in the order."""
        return len(self._items)

    def get_total(self):
        """Return the total cost of the order."""
        total = 0.0
        for item in self._items:
            if isinstance(item, Drink):
                total += 5.00  # Fixed price per drink
            elif isinstance(item, Food):
                total += item.get_price()
        return total


class TestDrink(unittest.TestCase):
    """Tests for the Drink class."""

    def test_add_base(self):
        """Test that a valid base can be added to a drink."""
        drink = Drink()
        drink.add_base("water")
        self.assertEqual(drink.get_base(), "water")

    def test_invalid_base(self):
        """Test that adding an invalid base raises a ValueError."""
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.add_base("invalid_base")

    def test_add_flavor(self):
        """Test that a valid flavor can be added to a drink."""
        drink = Drink()
        drink.add_flavor("lemon")
        self.assertIn("lemon", drink.get_flavors())

    def test_duplicate_flavor(self):
        """Test that adding a duplicate flavor raises a ValueError."""
        drink = Drink()
        drink.add_flavor("lemon")
        with self.assertRaises(ValueError):
            drink.add_flavor("lemon")


class TestFood(unittest.TestCase):
    """Tests for the Food class."""

    def test_add_topping(self):
        """Test that a valid topping can be added to a food item."""
        food = Food("Hotdog")
        food.add_topping("Chili")
        self.assertIn("Chili", food.get_toppings())

    def test_invalid_topping(self):
        """Test that adding an invalid topping raises a ValueError."""
        food = Food("Hotdog")
        with self.assertRaises(ValueError):
            food.add_topping("InvalidTopping")

    def test_get_price(self):
        """Test that the price of a food item is calculated correctly."""
        food = Food("Hotdog")
        food.add_topping("Chili")
        self.assertAlmostEqual(food.get_price(), 2.30 + 0.60)


class TestOrder(unittest.TestCase):
    """Tests for the Order class."""

    def test_add_items(self):
        """Test that items can be added to an order."""
        order = Order()
        drink = Drink()
        drink.add_base("water")
        order.add_item(drink)
        self.assertEqual(order.get_num_items(), 1)

    def test_get_total(self):
        """Test that the total cost of an order is calculated correctly."""
        order = Order()
        drink = Drink()
        drink.add_base("water")
        food = Food("Hotdog")
        food.add_topping("Chili")
        order.add_item(drink)
        order.add_item(food)
        self.assertAlmostEqual(order.get_total(), 5.00 + 2.30 + 0.60)

    def test_remove_item(self):
        """Test that an item can be removed from an order."""
        order = Order()
        drink = Drink()
        drink.add_base("water")
        order.add_item(drink)
        order.remove_item(0)
        self.assertEqual(order.get_num_items(), 0)


if __name__ == "__main__":
    unittest.main()
