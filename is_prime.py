#Prime number checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number %i == 0:
            is_prime = False
    if is_prime == False:
        print("It's not prime number")
    else:
        print("It's a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
