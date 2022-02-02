# a prime number can't be broken down into smaller parts other than one and itself


def prime_checker(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        return True
    return False


n = int(input("Check this number: "))
if prime_checker(number=n):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
