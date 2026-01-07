import sys


def main():
    """Analyzes player scores provided as command-line arguments."""
    print("=== Player Score Analytics ===")
    scores = []
    if (len(sys.argv) < 2):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    for line in range(1, len(sys.argv)):
        try:
            score = int(sys.argv[line])
            scores.append(score)
        except ValueError:
            print(f"Ignoring invalid score: {sys.argv[line]}")
    totalPlayers = len(scores)
    totalScore = sum(scores)
    average = sum(scores) / len(scores)
    highScore = max(scores)
    lowScore = min(scores)
    rangeScore = highScore - lowScore
    print("processed scores:", scores)
    print(f"Total players: {totalPlayers}")
    print(f"Total score: {totalScore}")
    print(f"Average score: {average:.1f}")
    print(f"High score: {highScore}")
    print(f"Low score: {lowScore}")
    print(f"Score range: {rangeScore}")


if __name__ == "__main__":
    main()
