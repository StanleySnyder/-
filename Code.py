import os

FILENAME = "phonebook.txt"

def load_phonebook():
    phonebook = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    phonebook.append({
                        "surname": parts[0],
                        "name": parts[1],
                        "patronymic": parts[2],
                        "phone": parts[3]
                    })
    return phonebook

def save_phonebook(phonebook):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for entry in phonebook:
            line = f"{entry['surname']},{entry['name']},{entry['patronymic']},{entry['phone']}\n"
            file.write(line)

def add_entry(phonebook):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    phonebook.append({
        "surname": surname,
        "name": name,
        "patronymic": patronymic,
        "phone": phone
    })
    save_phonebook(phonebook)
    print("Запись добавлена.")

def show_phonebook(phonebook):
    for entry in phonebook:
        print(f"{entry['surname']} {entry['name']} {entry['patronymic']}: {entry['phone']}")

def find_entry(phonebook, search_term):
    results = []
    for entry in phonebook:
        if (search_term.lower() in entry['surname'].lower() or
            search_term.lower() in entry['name'].lower() or
            search_term.lower() in entry['patronymic'].lower() or
            search_term.lower() in entry['phone'].lower()):
            results.append(entry)
    return results

def update_entry(phonebook):
    search_term = input("Введите фамилию или имя для поиска записи, которую хотите изменить: ")
    results = find_entry(phonebook, search_term)
    if results:
        print("Найденные записи:")
        for idx, entry in enumerate(results):
            print(f"{idx + 1}. {entry['surname']} {entry['name']} {entry['patronymic']}: {entry['phone']}")
        choice = int(input("Введите номер записи, которую хотите изменить: ")) - 1
        if 0 <= choice < len(results):
            entry = results[choice]
            print("Введите новые данные (оставьте поле пустым, чтобы не изменять его):")
            surname = input(f"Фамилия ({entry['surname']}): ") or entry['surname']
            name = input(f"Имя ({entry['name']}): ") or entry['name']
            patronymic = input(f"Отчество ({entry['patronymic']}): ") or entry['patronymic']
            phone = input(f"Телефон ({entry['phone']}): ") or entry['phone']
            entry.update({
                "surname": surname,
                "name": name,
                "patronymic": patronymic,
                "phone": phone
            })
            save_phonebook(phonebook)
            print("Запись обновлена.")
        else:
            print("Неверный выбор.")
    else:
        print("Записи не найдены.")

def delete_entry(phonebook):
    search_term = input("Введите фамилию или имя для поиска записи, которую хотите удалить: ")
    results = find_entry(phonebook, search_term)
    if results:
        print("Найденные записи:")
        for idx, entry in enumerate(results):
            print(f"{idx + 1}. {entry['surname']} {entry['name']} {entry['patronymic']}: {entry['phone']}")
        choice = int(input("Введите номер записи, которую хотите удалить: ")) - 1
        if 0 <= choice < len(results):
            phonebook.remove(results[choice])
            save_phonebook(phonebook)
            print("Запись удалена.")
        else:
            print("Неверный выбор.")
    else:
        print("Записи не найдены.")

def main():
    phonebook = load_phonebook()
    
    while True:
        print("\nТелефонный справочник:")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Найти запись")
        print("4. Изменить запись")
        print("5. Удалить запись")
        print("6. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            show_phonebook(phonebook)
        elif choice == "2":
            add_entry(phonebook)
        elif choice == "3":
            search_term = input("Введите фамилию, имя или отчество для поиска: ")
            results = find_entry(phonebook, search_term)
            if results:
                for entry in results:
                    print(f"{entry['surname']} {entry['name']} {entry['patronymic']}: {entry['phone']}")
            else:
                print("Записи не найдены.")
        elif choice == "4":
            update_entry(phonebook)
        elif choice == "5":
            delete_entry(phonebook)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
