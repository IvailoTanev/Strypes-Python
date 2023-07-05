


# 1. Sum of all digits of a number
def sum_of_digits(num):
    num_of_digits = 0
    new_num = num
    
    for iter in range(0, num):
        num = num // 10
        num_of_digits = num_of_digits + num % 10

    for iter in range(0, 5):
        result = result + new_num % 10
        new_num = new_num // 10
   

    return result
print(sum_of_digits(12000))


#2. Turn a number into a list of digits
#def to_digits(n):

