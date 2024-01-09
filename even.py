# 5. Write a program that reads a list of numbers and prints only the even numbers.



a  = [1,2,3,4,5,6,7]
l = [x for x in a if x % 2 == 0]

print(l)


# when user give the input


given_number = input("enter an nnumberwith a space: ")

numbers = [int(num) for num in given_number.split()]        #given_number.split() ==> Split the input string into a list of string And int(num) for num ==> this will convert string to int
even_number = [num for num in numbers if num % 2 == 0]
print(even_number)


#  i will use try except for invalid input1