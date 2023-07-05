


# 1. Sum of all digits of a number
def sum_of_digits(num):

    for iter in range(0, 5):
        result = result + num % 10
        num = num // 10
   
    return result
print(sum_of_digits(1200))


#2. Turn a number into a list of digits
#def to_digits(n):

