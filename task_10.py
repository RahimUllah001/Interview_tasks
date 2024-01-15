# 10. Write a function that generates the first 'n' terms of the Fibonacci sequence.

def fibo(limit):
        
    f = [0,1]
    for i in range(limit - 2):
        f_next = f[-1] + f[-2]
        f.append(f_next)

    print(f)    
        
fibo(20)




