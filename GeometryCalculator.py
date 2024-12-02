import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius

if __name__ == "__main__":
    calculator = GeometryCalculator()
    radius = 5
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius):.2f}")
