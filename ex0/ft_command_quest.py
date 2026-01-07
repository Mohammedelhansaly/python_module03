import sys


def main():
    """A simple command-line argument parser
    that prints the program name and its arguments."""
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    try:
        if (len(sys.argv) < 2):
            raise ValueError("No arguments provided!")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    except ValueError as e:
        print(e)
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
