# Консольний бот-помічник

def parse_input(user_input: str):
    """
    Розбирає рядок на команду та аргументи.
    Команда завжди перетворюється до нижнього регістру.
    """
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


def add_contact(args: list, contacts: dict) -> str:
    """
    Додає новий контакт до словника.
    Формат: add name phone
    """
    if len(args) != 2:
        return "Error: use format -> add name phone"

    name, phone = args
    contacts[name] = phone
    return "Contact added"


def change_contact(args: list, contacts: dict) -> str:
    """
    Змінює номер телефону існуючого контакту.
    Формат: change name phone
    """
    if len(args) != 2:
        return "Error: use format -> change name phone"

    name, phone = args

    if name not in contacts:
        return "Error: contact not found"

    contacts[name] = phone
    return "Contact updated"


def show_phone(args: list, contacts: dict) -> str:
    """
    Повертає номер телефону за іменем.
    Формат: phone name
    """
    if len(args) != 1:
        return "Error: use format -> phone name"

    name = args[0]

    if name not in contacts:
        return "Contact not found"

    return contacts[name]


def show_all(contacts: dict) -> str:
    """
    Виводить усі збережені контакти.
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

    print("Welcome to the assistant botруддщ")

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
