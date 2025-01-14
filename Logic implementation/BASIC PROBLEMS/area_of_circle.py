class CIRCLE:
    def __init__(self,radius):
        self.radius = radius
        self.PI = 3.14159

    def calculate_area(self):
        return self.PI * self.radius ** 2
    
def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = CIRCLE(radius)
    area = circle.calculate_area()
    print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()

