def calculate_inventory_value(item):
    total_value = item['quantity'] * item['value']
    return total_value


def total_inventory_value(inventory):
    total_value = 0
    for item, details in inventory.items():
        total_value += calculate_inventory_value(details)
    return total_value


def total_item_count(inventory):
    count = 0
    for item, details in inventory.items():
        count += details['quantity']
    return count


def rarest_items(*inventories):
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


def create_inventory(type, rarity, value, quantity):
    return {
        'type': type,
        'rarity': rarity,
        'value': value,
        'quantity': quantity
    }


def inventory_system():
    player1 = "Alice"
    player1_inventory = {
        'sword': create_inventory('weapon', 'rare', 500, 1),
        'potion': create_inventory('consumable', 'common', 50, 5),
        'shield': create_inventory('armor', 'uncommon', 200, 1)
        }
    player2 = "Bob"
    player2_inventory = {
        'sword': create_inventory('weapon', 'uncommon', 300, 1),
        'magic_ring': create_inventory('armor', 'rare', 400, 1),
        'potion': create_inventory('consumable', 'common', 50, 0)
        }
    print("=== Player Inventory System ===\n")
    print(f"=== {player1}'s Inventory ===")
    for item, details in player1_inventory.items():
        print(f"{item} ({details['type']}, {details['rarity']}):"
              f" {details['quantity']}x @ {details['value']} gold each = "
              f"{calculate_inventory_value(details)} gold")

    print()
    print(f"Inventory value: {total_inventory_value(player1_inventory)} gold")
    print(f"Item count: {total_item_count(player1_inventory)} items")
    categories_count = {}
    for item in player1_inventory.values():
        cat = item["type"]
        qty = item["quantity"]
        categories_count[cat] = categories_count.get(cat, 0) + qty
    categories_str = ", ".join(f"{cat}({count})" for cat, count in
                               categories_count.items())

    print(f"Categories: {categories_str}\n")

    print(f"=== Transaction: {player1} gives {player2} 2 potions ===")
    transfer_quantity = 2
    if player1_inventory['potion']['quantity'] >= transfer_quantity:
        player1_inventory['potion']['quantity'] -= transfer_quantity
        player2_inventory['potion']['quantity'] += transfer_quantity
        print("Transaction successful.\n")
    else:
        print("Transaction failed: Not enough potions.\n")

    print("=== Updated Inventories ===")
    print(f"{player1} potions: {player1_inventory['potion']['quantity']}")
    print(f"{player2} potions: {player2_inventory['potion']['quantity']}")

    print("=== Inventory Analytics ===")
    alice_total_value = total_inventory_value(player1_inventory)
    bob_total_value = total_inventory_value(player2_inventory)
    if (alice_total_value > bob_total_value):
        print(f"Most valuable player: {player1} ({alice_total_value} gold)")
    else:
        print(f"Most valuable player: {player2} ({bob_total_value} gold)")
    print(f"Most items: {player1} ({total_item_count(player1_inventory)}"
          f" items)")
    print(f"Rarest items: "
          f"{rarest_items(player1_inventory, player2_inventory)}")


if __name__ == "__main__":
    inventory_system()
