class Player:
    """Class to represent a player and their achievements."""
    def __init__(self, name) -> None:
        """Initialize the player with a name
        and an empty set of achievements."""
        self.name = name
        self.acheivements = set()

    def add_achievements(self, *achievements) -> None:
        """Add multiple achievements to the player's set."""
        for achievement in achievements:
            self.acheivements.add(achievement)

    def display_achievements(self) -> None:
        """Display the player's achievements."""
        print(f"Player {self.name} achievements: {self.acheivements}")


def main() -> None:
    """Demonstrate the achievement tracker system"""
    player1 = Player("alice")
    player1.add_achievements('first_kill', 'level_10', 'treasure_hunter',
                             'speed_demon')
    player2 = Player("bob")
    player2.add_achievements('first_kill', 'level_10', 'boss_slayer',
                             'collector')
    player3 = Player("charlie")
    player3.add_achievements('level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist')
    print("=== Achievement Tracker System ===\n")
    player1.display_achievements()
    player2.display_achievements()
    player3.display_achievements()
    print()
    print("=== Achievement Analytics ===")
    inters = player1.acheivements.intersection(player2.acheivements)
    diff1 = player1.acheivements.difference(player2.acheivements)
    diff2 = player2.acheivements.difference(player1.acheivements)
    print("\n=== Achievement Analytics ===")
    all = player1.acheivements.union(player2.acheivements).union(
          player3.acheivements)
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")
    print()
    all_common = player1.acheivements.intersection(
                 player2.acheivements).intersection(
                 player3.acheivements)
    shared_achievements = (
        player1.acheivements.intersection(player2.acheivements)
        .union(player1.acheivements.intersection(player3.acheivements))
        .union(player2.acheivements.intersection(player3.acheivements))
    )
    print(f"Common to all players: {all_common}")
    print(f"Rare achievements (1 player): {all - shared_achievements}")
    print()
    print(f"Alice vs Bob common:{inters}")
    print(f"Alice unique::{diff1}")
    print(f"Bob unique::{diff2}\n")


if __name__ == "__main__":
    main()
