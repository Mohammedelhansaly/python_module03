class Player:
    """Class to manage a player's inventory in a game."""
    def __init__(self, name) -> None:
        """Initialize the player with a name and an empty inventory."""
        self.name = name
        self.inventory = {}

    def create_inventory(self, type, rarity, value, quantity) -> dict:
        """Create an inventory item with specified attributes."""
        return {
            'type': type,
            'rarity': rarity,
            'value': value,
            'quantity': quantity
        }

    def add_item(self, item_name, type, rarity, value, quantity) -> None:
        """Add an item to the player's inventory."""
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = self.create_inventory(type, rarity,
                                                              value, quantity)

    def calculate_inventory_value(self, item) -> int:
        """Calculate the total value of a given inventory item."""
        total_value = item['quantity'] * item['value']
        return total_value

    def total_inventory_value(self) -> int:
        """Calculate the total value of the player's entire inventory."""
        total_value = 0
        for item, details in self.inventory.items():
            total_value += self.calculate_inventory_value(details)
        return total_value

    def total_item_count(self) -> int:
        """Calculate the total number of items in the player's inventory."""
        count = 0
        for item, details in self.inventory.items():
            count += details['quantity']
        return count

    @staticmethod
    def rarest_items(*inventories) -> str:
        """Determine the rarest items across multiple inventories."""
        rarity_order = {"common": 1, "uncommon": 2, "rare": 3, "legendary": 4}
        max_level = 0
        rare_items = set()

        for inventory in inventories:
            for name, item in inventory.items():
                level = rarity_order[item["rarity"]]
                if level > max_level:
                    max_level = level
                    rare_items = {name}
                elif level == max_level:
                    rare_items.add(name)

        return ", ".join(sorted(rare_items))

    def display_inventory(self) -> None:
        """Display the player's inventory in a readable format."""
        for item, details in self.inventory.items():
            print(f"{item} ({details['type']}, {details['rarity']}):"
                  f" {details['quantity']}x @ {details['value']} gold each = "
                  f"{self.calculate_inventory_value(details)} gold")

    def categories_str(self) -> str:
        """Generate a string summarizing item categories and their counts."""
        categories_count = {}
        for item in self.inventory.values():
            cat = item["type"]
            qty = item["quantity"]
            categories_count[cat] = categories_count.get(cat, 0) + qty
        categories_str = ", ".join(f"{cat}({count})" for cat, count in
                                   categories_count.items())
        return categories_str


def main() -> None:
    """Demonstrate the player inventory system."""
    player1 = Player("Alice")
    player1.add_item("sword", "weapon", "rare", 500, 1)
    player1.add_item("potion", "consumable", "common", 50, 5)
    player1.add_item("shield", "armor", "uncommon", 200, 1)

    player2 = Player("Bob")
    player2.add_item("magic_ring", "weapon", "rare", 100, 1)

    print("=== Player Inventory System ===\n")
    print(f"=== {player1.name}'s Inventory ===")
    player1.display_inventory()
    print()
    print(f"Inventory value: {player1.total_inventory_value()} gold")
    print(f"Item count: {player1.total_item_count()} items")
    print(f"Categories: {player1.categories_str()}")
    print()
    print(f"=== Transaction: {player1.name} gives {player2.name} "
          f"2 potions ===")
    if (
        "potion" in player1.inventory
        and player1.inventory["potion"]["quantity"] >= 2
    ):
        player1.inventory["potion"]["quantity"] -= 2
        player2.add_item("potion", "consumable", "common", 50, 2)
        print("Transaction successful!")
    else:
        print("Transaction failed: Not enough potions.")
    print()
    print("=== Updated Inventories ===")
    print(f"{player1.name} potions: {player1.inventory["potion"]["quantity"]}")
    print(f"{player2.name} potions: {player2.inventory["potion"]["quantity"]}")
    print()
    print("=== Inventory Analytics ===")
    if player1.total_inventory_value() > player2.total_inventory_value():
        print(f"Most valuable player: {player1.name} "
              f"({player1.total_inventory_value()} gold)")
    else:
        print(f"Most valuable player: {player2.name} "
              f"({player2.total_inventory_value()} gold)")
    if player1.total_item_count() > player2.total_item_count():
        print(f"Most items: {player1.name} "
              f"({player1.total_item_count()} items)")
    else:
        print(f"Most items: {player2.name}"
              f" ({player2.total_item_count()} items)")
    print(f"Rarest items:"
          f" {Player.rarest_items(player1.inventory, player2.inventory)}")


if __name__ == "__main__":
    main()
