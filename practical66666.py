def get_proper_factors(n):
    """Return a list of proper factors of n."""
    return [i for i in range(1, n) if n % i == 0]

def is_abundant(n):
    """Check if a number is abundant."""
    return sum(get_proper_factors(n)) > n

def is_deficient(n):
    """Check if a number is deficient."""
    return sum(get_proper_factors(n)) < n

def generate_abundant_until_first_odd():
    n = 1
    abundant_numbers = []
    found_odd_abundant = False

    while not found_odd_abundant:
        if is_abundant(n):
            abundant_numbers.append(n)
            if n % 2 == 1:
                found_odd_abundant = True
        n += 1

    return abundant_numbers

def print_deficient_up_to_100():
    deficient_numbers = [n for n in range(2, 101) if is_deficient(n)]
    print("Deficient numbers from 2 to 100:")
    print(deficient_numbers)

# Run both parts
abundant_list = generate_abundant_until_first_odd()
print("Abundant numbers up to and including the first odd abundant number:")
print(abundant_list)

print()  # Add a newline for separation

print_deficient_up_to_100()


def fibonacci_not_less_than_m(m):
    a, b = 0, 1
    while a < m:
        a, b = b, a + b
    return a


def digit_sum_until_under_20(n):
    while n >= 20:
        n = sum(int(d) for d in str(n))
    return n


def is_divisible_by_3(n):
    reduced_sum = digit_sum_until_under_20(n)
    return reduced_sum % 3 == 0


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def sum_primes_between(a, b):
    return sum(i for i in range(a, b+1) if is_prime(i))


# Example usage:
if __name__ == "__main__":
    # 1. Fibonacci
    M = int(input("Enter a positive integer M: "))
    fib = fibonacci_not_less_than_m(M)
    print(f"The first Fibonacci number ≥ {M} is: {fib}")

    # 2. Divisibility by 3
    num = int(input("Enter a number to test for divisibility by 3: "))
    result = is_divisible_by_3(num)
    print(f"{num} is {'divisible' if result else 'not divisible'} by 3.")

    # 3. Sum of Primes
    A = int(input("Enter A (start of range): "))
    B = int(input("Enter B (end of range): "))
    prime_sum = sum_primes_between(A, B)
    print(f"The sum of prime numbers between {A} and {B} is: {prime_sum}")
