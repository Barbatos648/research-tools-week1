"""输出 1000 以内的所有质数。

用法：python code/primes.py
"""

LIMIT = 1000


def is_prime(number):
    """判断 number 是否为质数：大于 1 且只能被 1 和自身整除。"""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def main():
    primes = [number for number in range(2, LIMIT) if is_prime(number)]
    print(f"{LIMIT} 以内的质数共有 {len(primes)} 个：")
    print(" ".join(str(prime) for prime in primes))


if __name__ == "__main__":
    main()
