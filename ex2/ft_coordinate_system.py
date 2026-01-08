import math

def calculate_distance(point1:tuple, point2:tuple) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def parse_cordinates(cordinate_str: str) -> tuple:
    """Parse a string of coordinates in the format 'x,y,z' into a tuple of integers."""
    try:
        x, y, z = cordinate_str.split(',')
        return int(x), int(y), int(z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

def cordinate_system() -> None:
    """Demonstrate the coordinate system functions."""
    print("=== Game Coordinate System ===\n")
    point1 = (0,0,0)
    point2 = (10,20,5)
    print(f"Poisition created : {point2}")
    print(f"Distance between {point1} and {point2}: {calculate_distance(point1, point2):.2f}\n")

    point3 = "3,4,0"
    point3_coords = parse_cordinates(point3)
    print(f"Parsing coordinates: {point3}")
    print(f"Parsed position: {point3_coords}")
    print(f"Distance between {point1} and {point3_coords}: {calculate_distance(point1, point3_coords):.2f}\n")

    invalid_point = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {invalid_point}")
    parse_cordinates(invalid_point)
    x, y, z = point3_coords
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    cordinate_system()