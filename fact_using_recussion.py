# finding fsctorial iteratively
'''num = 5
r= 1
for i in range(num):
    r = r * num
    num  = num -1

print(r)
'''
# using recursive function
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


print(fact(3))