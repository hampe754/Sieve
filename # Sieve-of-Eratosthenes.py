# Sieve of Eratosthenes
# Author: Eli Hamp
# Tues Aug 2nd 2025



def remove_multiples(subject, numbers, upper_limit):
    check_mults = list(range(2,upper_limit))
    for number in check_mults:
        if subject * number in numbers:
            numbers.remove(subject * number)


def main():
    upper_limit = int(input("enter a the upper limit:"))
    numbers = list(range(2,upper_limit))
    for number in numbers:
        remove_multiples(number, numbers, upper_limit)
    print(numbers)


if __name__ == "__main__":
    main()

    