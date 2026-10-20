from .exceptions import NegativeValueError, NonIntegerError, NonNumericError, EmptyDataError

def factorial(n):
    if n < 0:
        raise NegativeValueError("Can't count the factorial of a negative number!")

    if n == 0:
        return 1

    f = 1
    for i in range(n):
        f *= (i + 1)

    return f


def gcd(a, b):
    try:
        int(a)
        int(b)
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    except ValueError:
        raise NonIntegerError("Numbers for counting GCD must be integer!")


def lcm(a, b):
    try:
        int(a)
        int(b)
        a, b, abs(a), abs(b)
        c = gcd(a, b)
        return (a * b) / c
    except ValueError:
        raise NonIntegerError("Numbers for counting LCM must be integer!")


def is_prime(n):
    try:
        int(n)
    except ValueError:
        raise NonIntegerError("Numbers to be checked for primality must be integer!")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def my_sqrt(n, tolerance=1e-7):
    try:
        float(n)
    except ValueError:
        raise NonNumericError("The input is not a number!")

    if n < 0:
        raise NegativeValueError("Can't count the root of a negative number!")
    if n == 0 or n == 1:
        return n

    low = 0.0
    high = max(1.0, n)

    while high - low > tolerance:
        mid = (high + low) / 2
        square = mid * mid

        if square > n:
            high = mid
        else:
            low = mid

    return (high + low) / 2


def cbrt(n, tolerance=1e-7):
    try:
        float(n)
    except ValueError:
        raise NonNumericError("The input is not a number!")

    if n == 0 or n == 1 or n == -1:
        return n
    abs_n = abs(n)

    low = 0.0
    high = max(abs_n, 1.0)
    while high - low > tolerance:
        mid = (high + low) / 2
        cube = mid * mid * mid

        if cube > abs_n:
            high = mid
        else:
            low = mid
    result = (high + low) / 2
    return -result if n < 0 else result

def my_sum(data):
    if not data:
        raise EmptyDataError("Data is empty!")

    total = 0
    for value in data:
        total += value

    return total


def cumsum(data):
    if not data:
        EmptyDataError("Data is empty!")

    cum_data = [data[0]]
    for i, value in enumerate(data[1:], start=1):
        cum_data.append(cum_data[i - 1] + value)
    return cum_data


def product(data):
    if not data:
        EmptyDataError("Data is empty!")

    total = 1
    for value in data:
        total *= value
    return total


def my_pow(n, x):
    try:
        int(x)
    except ValueError:
        raise NonIntegerError("Power must be integer!")
    try:
        float(n)
    except ValueError:
        raise NonNumericError("The input is not a number!")

    if x == 0 or n == 1:
        return 1.0
    if n == 0:
        if x <= 0:
            raise NegativeValueError("0 power mustn't be negative!")
        return 0.0

    if x < 0:
        x = -x
        n = 1.0 / n

    result = 1
    current_product = n
    while x > 0:
        if x % 2 == 1:
            result *= current_product

        current_product *= current_product
        x /= 2
    return result


def get_PI():
    pi = 0
    k = 1
    for i in range(1000000):
        if i % 2 == 0:
            pi += 4 / k
        else:
            pi -= 4 / k
        k += 2

    return pi
