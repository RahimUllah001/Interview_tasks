# . Based on user input, write a Python script to calculate the area of different geometric shapes (circle, triangle, square)


shape = input("Area of which quantit u want ot calculate:")

if shape == "circle":
    radius = int(input("plz enter the radius of the circle: "))
    Area = (22/7) * radius * radius
    print(Area)
elif shape == "triangle":
    height = int(input("plz enter the hieght of triangle: "))
    base = int(input("plz enter the base of triangle: "))
    Area_of_triangle = 1/2 * height * base
    print(Area_of_triangle)
    
elif shape == "square":
    length = int(input("plz enter the lenght of one side: "))
    Area_of_square = length * length
    print(Area_of_square)
else:
    print("Invalid input or spelling mistake")
   
