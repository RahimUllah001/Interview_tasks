#Create a function that calculates the sum of all even Fibonacci numbers up to a given limit

fib_sequence = [0,1]

def fiboo(limit):
    while True:
        fib_next = fib_sequence[-1] + fib_sequence[-2]
        if fib_next > limit:
            break
        fib_sequence.append(fib_next)
    
    even_sum =sum( [x for x in fib_sequence if x%2 == 0])
    print(even_sum)#required ans


fiboo(60)
print(fib_sequence)