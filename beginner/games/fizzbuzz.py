
for n in range(1, 101):
    div_3 = True if n % 3 == 0 else False
    div_5 = True if n % 5 == 0 else False
    div_both = True if n % 3 == 0 and n % 5 == 0 else False

    if div_both:
        print("FizzBuzz")
        continue

    if div_5:
        print("Buzz")
        continue

    if div_3:
        print("Fizz")
        continue

    print(n)
