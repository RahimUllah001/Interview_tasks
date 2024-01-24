# 18. Implement a function that computes two numbers' LCM (Least Common Multiple).
# formula for lcm a * b / gcd

def lcm_of(x,y):

    def gcd(a,b):

        while b:
            a, b = b, a % b
        return a
    return abs(x * y) // gcd(x, y)


a = 12000
b = 18000

reslut  = lcm_of(a, b)
print(reslut)

