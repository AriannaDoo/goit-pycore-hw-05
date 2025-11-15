# ПСЕВДОКОД (опис алгоритму)
# ============================================

# ФУНКЦІЯ caching_fibonacci
#     Створити порожній словник cache
#
#     ФУНКЦІЯ fibonacci(n)
#         Якщо n <= 0, повернути 0
#         Якщо n == 1, повернути 1
#         Якщо n у cache, повернути cache[n]
#
#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]
#
#     Повернути функцію fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci


# РЕАЛІЗАЦІЯ ПСЕВДОКОДУ НА PYTHON
# ============================================

from typing import Callable, Dict

def caching_fibonacci() -> Callable[[int], int]:
    """
    Повертає внутрішню функцію fibonacci(n),
    яка обчислює n-те число Фібоначчі з кешуванням (замиканням).
    """

    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Тестовий виклик з прикладу
if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))   # 55
    print(fib(15))   # 610
