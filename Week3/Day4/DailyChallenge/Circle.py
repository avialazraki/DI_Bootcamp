
# ============================================
# Week 3 - Day 4 - Daily Challenge
# Circle Class - OOP and Dunder Methods
# ============================================

import math


class Circle:

    # Create a circle using its radius
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        self.radius = radius

    # Decorator: Create a circle using its diameter
    @classmethod
    def from_diameter(cls, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative.")

        return cls(diameter / 2)

    # Get or update the diameter
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        if value < 0:
            raise ValueError("Diameter cannot be negative.")

        self.radius = value / 2

    # Calculate the circle's area
    def area(self):
        return math.pi * self.radius ** 2

    # Display the circle's attributes
    def __str__(self):
        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter}, "
            f"area={self.area():.2f})"
        )

    # Add two circles and return a new circle
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return Circle(self.radius + other.radius)

    # Compare whether one circle is bigger
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius > other.radius

    # Compare whether two circles are equal
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius == other.radius

    # Allow sorting circles from smallest to largest
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius < other.radius


# ============================================
# Test the Circle class
# ============================================

print("Week 3 - Day 4 - Daily Challenge")

# Create circles using radius and diameter
circle1 = Circle(5)
circle2 = Circle.from_diameter(8)
circle3 = Circle(3)
circle4 = Circle.from_diameter(10)

print("\n1. Circle attributes:")
print(circle1)
print(circle2)
print(circle3)
print(circle4)

print("\n2. Circle area:")
print(f"Circle 1 area: {circle1.area():.2f}")

print("\n3. Add two circles:")
circle5 = circle1 + circle2
print(circle5)

print("\n4. Compare circle sizes:")
print("Circle 1 > Circle 2:", circle1 > circle2)

print("\n5. Check equality:")
print("Circle 1 == Circle 4:", circle1 == circle4)

print("\n6. Sort circles:")
circles = [circle1, circle2, circle3, circle4]
sorted_circles = sorted(circles)

for circle in sorted_circles:
    print(circle)

print("\n7. Test diameter setter:")
circle3.diameter = 12
print(circle3)
