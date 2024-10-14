# Функція для завантаження списку покупок з файлу
def load_shopping_list(filename):
    shopping_list = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                product, quantity = line.strip().split(', ')
                shopping_list[product] = int(quantity)
    except FileNotFoundError:
        # Якщо файл не існує, ми просто повертаємо порожній список
        print(f"Файл {filename} не знайдено, створюється новий список.")
    return shopping_list

# Функція для збереження списку покупок у файл
def save_shopping_list(filename, shopping_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for product, quantity in shopping_list.items():
            file.write(f"{product}, {quantity}\n")

# Функція для перегляду списку покупок
def view_shopping_list(shopping_list):
    if not shopping_list:
        print("Список покупок порожній.")
    else:
        for product, quantity in shopping_list.items():
            print(f"{product}: {quantity}")

# Функція для додавання нового продукту до списку
def add_product(shopping_list):
    product = input("Введіть назву продукту: ")
    if product in shopping_list:
        print(f"{product} вже є у списку. Використайте функцію редагування.")
    else:
        quantity = int(input("Введіть кількість: "))
        shopping_list[product] = quantity
        print(f"{product} додано з кількістю {quantity}.")

# Функція для редагування продукту
def edit_product(shopping_list):
    product = input("Введіть назву продукту, який потрібно редагувати: ")
    if product in shopping_list:
        quantity = int(input(f"Введіть нову кількість для {product}: "))
        shopping_list[product] = quantity
        print(f"Кількість для {product} змінено на {quantity}.")
    else:
        print(f"{product} не знайдено у списку.")

# Функція для видалення продукту зі списку
def delete_product(shopping_list):
    product = input("Введіть назву продукту, який потрібно видалити: ")
    if product in shopping_list:
        del shopping_list[product]
        print(f"{product} видалено зі списку.")
    else:
        print(f"{product} не знайдено у списку.")

# Основна функція програми
def main():
    filename = "shopping_list.txt"
    shopping_list = load_shopping_list(filename)

    while True:
        print("\n1. Переглянути список покупок")
        print("2. Додати продукт")
        print("3. Редагувати продукт")
        print("4. Видалити продукт")
        print("5. Зберегти зміни та вийти")
        choice = input("Виберіть дію (1-5): ")

        if choice == '1':
            view_shopping_list(shopping_list)
        elif choice == '2':
            add_product(shopping_list)
        elif choice == '3':
            edit_product(shopping_list)
        elif choice == '4':
            delete_product(shopping_list)
        elif choice == '5':
            save_shopping_list(filename, shopping_list)
            print("Зміни збережено. Вихід із програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == '__main__':
    main()