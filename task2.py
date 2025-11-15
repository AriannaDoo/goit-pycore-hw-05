from typing import Callable, Generator
import re


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту як float.
    """
    pattern = r"\b\d+(?:\.\d+)?\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, використовуючи генератор чисел з тексту.
    """
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
