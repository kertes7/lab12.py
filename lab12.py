# task 1

inventory = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 15000, "категорія": "електроніка"},
    {"назва": "Мишка", "кількість": 25, "ціна": 400, "категорія": "електроніка"},
    {"назва": "Футболка", "кількість": 50, "ціна": 300, "категорія": "одяг"},
    {"назва": "Кава", "кількість": 5, "ціна": 120, "категорія": "продукти"},
    {"назва": "Чай", "кількість": 2, "ціна": 80, "категорія": "продукти"},
    {"назва": "Штани", "кількість": 20, "ціна": 700, "категорія": "одяг"},
    {"назва": "Навушники", "кількість": 15, "ціна": 800, "категорія": "електроніка"}
]

print("{:<15} {:<10} {:<10} {:<12}".format("Назва", "Кількість", "Ціна", "Категорія"))
for item in inventory:
    print("{:<15} {:<10} {:<10} {:<12}".format(item["назва"], item["кількість"], item["ціна"], item["категорія"]))


#task 2

inventory = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 15000, "категорія": "електроніка"},
    {"назва": "Мишка", "кількість": 25, "ціна": 400, "категорія": "електроніка"},
    {"назва": "Футболка", "кількість": 50, "ціна": 300, "категорія": "одяг"},
    {"назва": "Кава", "кількість": 5, "ціна": 120, "категорія": "продукти"},
    {"назва": "Чай", "кількість": 2, "ціна": 80, "категорія": "продукти"},
    {"назва": "Штани", "кількість": 20, "ціна": 700, "категорія": "одяг"},
    {"назва": "Навушники", "кількість": 15, "ціна": 800, "категорія": "електроніка"}
]


def find_and_edit(inventory):
    key = input("Пошук за (назва/категорія): ").strip().lower()
    if key not in ["назва", "категорія"]:
        print("Неправильний параметр.")
        return

    value = input(f"Введіть значення для пошуку ({key}): ").strip().lower()
    found = [item for item in inventory if item[key].lower() == value]

    if not found:
        print("Товар не знайдено.")
        return

    for item in found:
        print(f"Знайдено: {item}")
        try:
            change = input("Оновити кількість чи ціну? (кількість/ціна/ні): ").strip().lower()
            if change == "кількість":
                new_qty = int(input("Нова кількість: "))
                item["кількість"] = new_qty
            elif change == "ціна":
                new_price = float(input("Нова ціна: "))
                item["ціна"] = new_price
        except Exception as e:
            print("Помилка при оновленні:", e)

find_and_edit(inventory)

#task 3

# Завдання 3: аналітика по категоріях

from collections import defaultdict

category_values = defaultdict(float)
low_stock = []

threshold = 5

for item in inventory:
    total = item["кількість"] * item["ціна"]
    category_values[item["категорія"]] += total
    if item["кількість"] < threshold:
        low_stock.append(item)

print("\nЗагальна вартість по категоріях:")
for cat, val in category_values.items():
    print(f"{cat}: {val:.2f} грн")

if category_values:
    top_category = max(category_values, key=category_values.get)
    print("\nКатегорія з найбільшою вартістю:", top_category)

print("\nТовари з кількістю нижче", threshold)
for item in low_stock:
    print(f"{item['назва']} ({item['кількість']} шт.)")

