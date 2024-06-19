class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        items_str = ', '.join([f"{item}: ${price}" for item, price in self.items.items()])
        return f"Магазин: {self.name}\nАдрес: {self.address}\nАссортимент: {items_str if items_str else 'пусто'}"

# Создание объектов класса Store
store1 = Store("Магазин №1", "ул. Пушкина, д. 1")
store2 = Store("Магазин №2", "ул. Лермонтова, д. 2")
store3 = Store("Магазин №3", "ул. Чехова, д. 3")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("молоко", 1.0)
store2.add_item("хлеб", 0.8)

store3.add_item("сыр", 2.5)
store3.add_item("масло", 1.5)

# Вывод информации о магазинах
print(store1)
print(store2)
print(store3)

# Тестирование методов на одном из магазинов
print("\nТестирование методов для Магазин №1:")

# Добавление товара
store1.add_item("апельсины", 1.2)
print("После добавления апельсинов:")
print(store1)

# Обновление цены товара
store1.update_price("яблоки", 0.55)
print("\nПосле обновления цены на яблоки:")
print(store1)

# Запрашивание цены товара
price = store1.get_price("бананы")
print(f"\nЦена на бананы: ${price}")

# Удаление товара
store1.remove_item("бананы")
print("\nПосле удаления бананов:")
print(store1)

# Попытка запрашивания цены на удаленный товар
price = store1.get_price("бананы")
print(f"\nЦена на бананы после удаления: {price}")  # Ожидается None