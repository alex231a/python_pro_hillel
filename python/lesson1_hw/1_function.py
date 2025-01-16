def calculate_circle_area(radius_value: str):
    """Calculate the area of a circle given its radius."""
    try:
        radius: float = float(radius_value)
        if radius < 0 or radius == 0:
            raise ValueError("Radius cannot be negative or 0.")
        area: float = 3.14 * radius ** 2
        return area
    except ValueError as ve:
        return str(ve)


radius_v = input("Enter radius value: ")

result = calculate_circle_area(radius_v)

print(f"The area of the circle is {result}")
