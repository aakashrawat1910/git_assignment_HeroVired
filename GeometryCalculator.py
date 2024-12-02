import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius  # Fixed the formula (r²)
    
    def calculate_rectangle_area(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()
    
    # Circle area calculation
    radius = 5
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius):.2f}")
    
    # Rectangle area calculation
    length = 10
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")