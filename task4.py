# Консольний бот-помічник з декоратором input_error

def input_error(func):
    """
    Декоратор для обробки помилок введення користувача
    Обробляє KeyError, ValueError, IndexError і повертає
    зрозумілі повідомлення замість траси помилки
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            # Наприклад, коли не вистачає name/phone при розпаковці
            return "Give me name and phone please"
        except IndexError:
            # Наприклад, коли користувач не передав аргументи взагалі
            return "Enter the argument for the command"

    return inner


def parse_input(user_input: str):
    """
    Розбирає рядок на команду та аргументи.
    Команда завжди перетворюється до нижнього регістру.
    """
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    """
    Додає новий контакт до словника.
    Формат: add name phone
    Тут свідомо не робимо перевірок,
    щоб помилки ловив саме декоратор.
    """
    name, phone = args  # якщо аргументів менше/більше → ValueError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    """
    Змінює номер телефону існуючого контакту.
    Формат: change name phone
    """
    name, phone = args  # тут теж можливий ValueError

    if name not in contacts:
        # Декоратор піймає KeyError і поверне "Contact not found"
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list, contacts: dict) -> str:
    """
    Повертає номер телефону за іменем.
    Формат: phone name
    """
    name = args[0]              # якщо args порожній → IndexError
    phone = contacts[name]      # якщо немає такого імені → KeyError
    return phone


def show_all(contacts: dict) -> str:
    """
    Виводить усі збережені контакти.
    Для цієї функції декоратор не обов'язковий,
    бо тут ми не очікуємо помилок введення.
    """
    if not contacts:
        return "No contacts saved"

    result = ["All saved contacts:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    """
    Основний цикл роботи бота.
    Обробляє введення користувача і викликає потрібні функції.
    """
    contacts = {}

    print("Welcome to the assistant bot")

    while True:
        user_input = input(">>> ")

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
