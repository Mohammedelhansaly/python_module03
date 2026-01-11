import random
import time


def game_event_stream(total_events):
    players = ["alice", "bob", "charlie", "dave"]
    events = [" killed monster", "found treasure", "leveled up"]
    for i in range(1, total_events + 1):
        player = random.choice(players)
        action = random.choice(events)
        level = random.randint(1, 20)
        yield {"id": i, "player": player, "event": action, "level": level}


def process_stream(total_events):
    start_time = time.time()
    high_level_events = 0
    treasure_events = 0
    level_up_events = 0
    for event in game_event_stream(total_events):
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player "
                  f"{event['player']} (level {event['level']}) "
                  f"{event['event']}")
        if event["level"] >= 10:
            high_level_events += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        if event["event"] == "leveled up":
            level_up_events += 1
    end_time = time.time()
    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_events}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime(n):
    num = 2
    count = 0
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    total_events = 1000
    process_stream(total_events)
    print("\n=== Generator Demonstration ===")
    fib_list = [str(num) for num in fibonacci(10)]
    print(f"Fibonacci sequence (first 10): {", ".join(fib_list)}")
    print(f"Prime numbers (first 5): "
          f"{', '.join(str(num) for num in prime(5))}")


if __name__ == "__main__":
    main()
