def prime_number_checker(num):
    factors = []
    is_prime = True
    for n in range(2, num):
        if num % n == 0:
            is_prime = False
            factors.append(n)

    if is_prime:
        print(f"{num} is a prime number")

    else:
        print(f"{num} is NOT a prime number")
        print(f"The factors of {num} are {factors}")


number = int(input("What is the number you want to check? "))
prime_number_checker(number)