# 14. Write a Python script to calculate a number's factorial without recursion.
num = 5
r= 1
for i in range(num):
    r = r * num
    num  = num -1

print(r)