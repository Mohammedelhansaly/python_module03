

def achievement_analytics():
    player1 = "alice"
    player1_achievements = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}

    player2 = "bob"
    player2_achievements=  {'first_kill', 'level_10', 'boss_slayer', 'collector'}

    player3 = "charlie"
    player3_achievements =  {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    
    print(f"Player: {player1} achievements: {player1_achievements}")
    print(f"Player: {player2} achievements: {player2_achievements}")
    print(f"Player: {player3} achievements: {player3_achievements}")
    inters = player1_achievements.intersection(player2_achievements)
    diff1 = player1_achievements.difference(player2_achievements)
    diff2 = player2_achievements.difference(player1_achievements)
    print("\n=== Achievement Analytics ===")
    all = player1_achievements.union(player2_achievements).union(player3_achievements)
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")
    print()
    all_common = player1_achievements.intersection(player2_achievements).intersection(player3_achievements)
    print(f"Common to all players: {all_common}")
    print(f"Rare achievements (1 player): {all - (player1_achievements.intersection(player2_achievements).union(player1_achievements.intersection(player3_achievements)).union(player2_achievements.intersection(player3_achievements)))}")
    print()
    print(f"Alice vs Bob common:{inters}")
    print(f"Alice unique::{diff1}")
    print(f"Bob unique::{diff2}\n")


if __name__ == "__main__":
    achievement_analytics()