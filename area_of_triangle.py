def area_of_triangle(base, height):
    """Calculate the area of a triangle given base and height."""
    return 0.5 * base * height

if __name__ == "__main__":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_of_triangle(base, height)
    print(f"The area of the triangle is {area}.")
