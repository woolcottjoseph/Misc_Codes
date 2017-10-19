def reverser(start_string):
    reversed_string = []
    for item in start_string:
        reversed_string[0:0] = item
    print ("".join(reversed_string))

reverser('Reverse me')

def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print (factorial(6))