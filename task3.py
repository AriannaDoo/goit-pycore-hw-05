import sys
from typing import List, Dict


def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок лог-файлу та повертає словник:
    {
        "date": "...",
        "time": "...",
        "level": "...",
        "message": "..."
    }
    """
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return None  # некоректний рядок

    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message
    }



def load_logs(file_path: str) -> List[dict]:
    """
    Зчитує усі рядки лог-файлу та перетворює їх у список словників.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Фільтрує записи за рівнем логування (INFO, ERROR, DEBUG, WARNING).
    """
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів за кожним рівнем логування.
    """
    counts = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}

    for log in logs:
        lvl = log["level"]
        if lvl in counts:
            counts[lvl] += 1

    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Виводить таблицю зі статистикою.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")


def main():
    # Перевірка кількості аргументів
    if len(sys.argv) < 2:
        print("Використання: python task3.py <path-to-logfile> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) == 3 else None

    # Завантажуємо лог-файл
    logs = load_logs(file_path)

    # Загальна статистика
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо вказаний рівень - показати деталі
    if level_filter:
        level_filter = level_filter.upper()
        filtered = filter_logs_by_level(logs, level_filter)

        print()
        print(f"Деталі логів для рівня '{level_filter}':")
        print("----------------------------------------")

        if not filtered:
            print("Немає записів цього рівня.")
        else:
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
