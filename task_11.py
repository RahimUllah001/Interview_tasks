# 11. Write a Python program that calculates the sum of all multiples of 7 from 1 to 100.
sum_multiples_of_7 = 0

for number in range(1, 101):
    if number % 7 == 0:
        sum_multiples_of_7 += number

print(f"The sum of all multiples of 7 from 1 to 100 is: {sum_multiples_of_7}")
