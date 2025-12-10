'''
                                        TASK:
    Implement one or more of the integer multiplication algorithms described
    in the lectures to find the product of the following 64-digit numbers:
    3141592653589793238462643383279502884197169399375105820974944592
    2718281828459045235360287471352662497757247093699959574966967627

    NOTE: I used the Karatsuba Multiplication method (only works for two 
    even-digit numbers of the same length)
'''

number1 = input("What is the first number? ") # Using user input instead of pre-defined numbers
number2 = input("What is the second number? ")

length = len(number1)
halfLength = int(length/2)

a = int(number1[:halfLength])
b = int(number1[-halfLength:])
c = int(number2[:halfLength])
d = int(number2[-halfLength:])

part1 = (a * c)
part2 = (b * d)
part3 = ((a + b) * (c + d))
part4 = (part3 - part2 - part1)
final = ((part1 * (10 ** (length))) + part2 + (part4 * (10 ** (halfLength))))

print(f"a x c = {part1}")
print(f"b x d = {part2}")
print(f"(a + b)(c + d) = {part3}")
print(f"(a + b)(c + d) - (b x d) - (a x c) = {part4}")
print(f"Therefore, the product of {number1} and {number2} is: {final}")