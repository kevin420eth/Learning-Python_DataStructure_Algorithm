#Calculating the Fibonacci series

#overlapping
def calFibonacci_array_1(length):
    fibonacci_array = []
    for _ in range(length):
        next_number = calFibonacci_number(_)
        fibonacci_array.append(next_number)
    return fibonacci_array

def calFibonacci_number(index):
    if index<=1:
        return 1
    else:
        return calFibonacci_number(index-1) + calFibonacci_number(index-2)

#----------------------How dynamic programming works----------------------#

#non-overlapping
def calFibonacci_array_2(length):
    fibonacci_array = []
    index=0
    while index<length:
        if len(fibonacci_array)<=1:
            fibonacci_array.append(1)
            index+=1
        else:
            next_number=fibonacci_array[index-1]+fibonacci_array[index-2]
            fibonacci_array.append(next_number)
            index+=1
    return fibonacci_array

print(calFibonacci_array_1(40))

# You can try calFibonacci_array_1 with some big input data, in my case, when length argument is bigger than 30,
# the run time becomes much more longer (My GPU is GTX-1060)