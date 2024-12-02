import math

class GeometryCalculator:
    def calculate_rectangle_area(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()
    length = 10
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
