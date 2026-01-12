class Player:
    """A class to represent a player in the game."""
    def __init__(self, name: str, score: int, region: str) -> None:
        """Initialize a Player instance."""
        self.name = name
        self.score = score
        self.region = region
        self.achievements = set()

    def add_achievement(self, *achievements) -> None:
        """Add achievements to the player's achievement set."""
        for achievement in achievements:
            self.achievements.add(achievement)


def highest_scorer(players: list[Player]) -> list[str]:
    """Return a list of names of players with scores >= 2000."""
    high_score = []
    for player in players:
        if player.score >= 2000:
            high_score.append(player.name)
    return high_score


def score_doubled(players: list[Player]) -> list[int]:
    """Return a list of players' scores doubled."""
    return [player.score * 2 for player in players]


def active_players(players: list[Player]) -> list[str]:
    """Return a list of names of players with scores > 1500."""
    return [player.name for player in players if player.score > 1500]


def score_dict(players: list[Player]) -> dict[str, int]:
    """Return a dictionary mapping player names to their scores."""
    return {player.name: player.score for player in players}


def score_category(players: list[Player]) -> dict[str, int]:
    """Categorize players based on their scores into
        'high', 'medium', and 'low'."""
    categories = {'high': 0, 'medium': 0, 'low': 0}
    for player in players:
        if player.score >= 2000:
            categories['high'] += 1
        elif 1500 <= player.score < 2000:
            categories['medium'] += 1
        else:
            categories['low'] += 1
    return categories


def acheivement_count(players: list[Player]) -> dict[str, int]:
    """Return a dictionary mapping player names to their"""
    return {player.name: len(player.achievements) for player in players}


def top_performer(players: list[Player]) -> dict[str, int]:
    """Return information about the top performer."""
    high_score = 0
    for player in players:
        if player.score >= high_score:
            high_score = player.score
            top_player = player
    return {
        'name': top_player.name,
        'score': high_score,
        'achievements': len(top_player.achievements)
    }


def main() -> None:
    """Main function to demonstrate the analytics dashboard."""
    player1 = Player("alice", 2300, "north")
    player1.add_achievement('first_kill', 'level_10', 'treasure_hunter',
                            'speed_demon')
    player2 = Player("bob", 1800, "east")
    player2.add_achievement('first_kill', 'level_10', 'boss_slayer',
                            'collector')
    player3 = Player("charlie", 2150, "central")
    player3.add_achievement('level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist')
    player4 = Player("diana", 2050, "north")
    player4.add_achievement('first_kill', 'level_10', 'treasure_hunter')

    players = [player1, player2, player3, player4]
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {highest_scorer(players)}")
    print(f"Scores doubled: {score_doubled(players)}")
    print(f"Active players: {active_players(players)}")
    print()
    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {score_dict(players)}")
    print(f"Score categories: {score_category(players)}")
    print(f"Achievement counts: {acheivement_count(players)}")
    print()
    print("=== Set Comprehension Examples ===")
    print(f"Unique players : {set(player.name for player in players)}")
    print(f"Unique achievements : "
          f"{set(ach for player in players for ach in player.achievements)}")
    print(f"Active regions : "
          f"{set(player.region for player in players if player.score > 1500)}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total Players: {len(players)}")
    total_achievements = set(
        ach for player in players for ach in player.achievements
    )
    print(f"Total unique achievements: {len(total_achievements)}")
    print(f"Average Score: "
          f"{sum(player.score for player in players) / len(players):.1f}")
    top_performer_info = top_performer(players)
    print(f"Top perfomer : {top_performer_info['name']} "
          f"({top_performer_info['score']} points, "
          f"{top_performer_info['achievements']} achievements)")


if __name__ == "__main__":
    main()
