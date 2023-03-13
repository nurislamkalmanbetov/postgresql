# import psycopg2 
# import os 

# postgres = psycopg2.connect(
#     dbname='my_bot', 
#     user='postgres', 
#     password='qwerty123', 
#     host='localhost',
#     port=5432
# )

# cursor = postgres.cursor()

# def get_all_product():
#     all_row = """
#         SELECT * FROM product;
#     """
#     cursor.execute(query=all_row)
#     all_product = cursor.fetchall()

#     for product in all_product:
#         print(product)

# def get_product_id(prod_id):
#     query = """
#         SELECT * FROM product
#         WHERE id = %s;
#         """
#     cursor.execute(query, (prod_id,))
#     product = cursor.fetchone()
#     if product:
#         product_date = product[3]
#         formated_date = product_date.strftime("%Y-%m-%d %H:%M:%S")
#         print(f"""ID: {product[0]}\nНазвание: {product[6]}\nЦена: {product[1]}\nОписание: {product[2]}
# Дата создания: {product[3]}\nКатегория: {product[4]}\nБрэнд: {product[5]}""")
#         return product
#     else:
#         return None

# def get_input_id():
#     prod_id = None
#     while True:
#         prod_id = input("Введите ID продукта: ")
#         if prod_id.isdigit():
#             break
#         else:
#             print("Ошибка! Введите цифры")
    

#     get_product_id(prod_id)


# # def get_product_brands_apple():
# #     product_phone_apple = """
# #         SELECT p.name, p.price, c.name as category, b.name as brand
# #         FROM product p
# #         JOIN brands b ON p.brand = b.id
# #         JOIN category c ON p.categories = c.id
# #         WHERE b.name = 'Apple';
# #     """
# #     cursor.execute(query=product_phone_apple)

# #     product = cursor.fetchall()
# #     for product in product:
# #         print(product)

# def get_product_brands_by_name(name):
#     product_brands_by_name = """
#         SELECT p.name, p.price, c.name as category, b.name as brand
#         FROM product p
#         JOIN brands b ON p.brand = b.id
#         JOIN category c ON p.categories = c.id
#         WHERE b.name = {};
#     """
#     cursor.execute(query=product_brands_by_name.format(name))

#     product = cursor.fetchall()
#     for product in product:
#         print(product)

# def get_product_category_laptops():
#     product_category_laptops = """
#         SELECT p.name, p.price, c.name as category, b.name as brand
#         FROM product p
#         JOIN brands b ON p.brand = b.id
#         JOIN category c ON p.categories = c.id
#         WHERE c.name = 'laptop';
#     """
#     cursor.execute(query=product_category_laptops)

#     product = cursor.fetchall()
#     for product in product:
#         print(product)

# def get_product_category_phones():
#     product_category_phones = """
#         SELECT p.name, p.price, c.name as category, b.name as brand
#         FROM product p
#         JOIN brands b ON p.brand = b.id
#         JOIN category c ON p.categories = c.id
#         WHERE c.name = 'phone';
#     """
#     cursor.execute(query=product_category_phones)

#     product = cursor.fetchall()
#     for product in product:
#         print(product)

# def get_product_category_smartwatches():
#     product_category_smartwatches = """
#         SELECT p.name, p.price, c.name as category, b.name as brand
#         FROM product p
#         JOIN brands b ON p.brand = b.id
#         JOIN category c ON p.categories = c.id
#         WHERE c.name = 'smart watches';
#     """
#     cursor.execute(query=product_category_smartwatches)

#     product = cursor.fetchall()
#     for product in product:
#         print(product)

# def get_delete_product_with_id(product_id):
#     product_id = """
#         SELECT * FROM product
#         WHERE id = {};
#         """
#     cursor.execute(query=product_id.format(product_id))
#     product = cursor.fetchone()
#     print(product)

# def get_delete_product_with_id():
#     product_id = input("Введите ID продукта: ")
#     get_product_id(product_id)

# def get_delete_product_with_id():
#     product_id = input("Введите ID продукта: ")
#     get_product_id(product_id)
#     answer = input("Удалить запись? Введите 'Yes', чтобы удалить: ")
#     if answer.lower() == "yes":
#         cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
#         print("Запись удалена успешно.")
#     else:
#         print("Удаление отменено.")

# def get_add_info():
#     name = input("Введите название продукта: ")
#     price = float(input("Введите цену продукта: "))
#     description = input("Введите описание продукта: ")
#     category = int(input("Введите ID категории продукта (4 для laptop, 5 для phone, 6 smart watches): "))
#     brand = int(input("Введите ID бренда продукта (26 для Samsung, 27 для Xiaomi, 28 для Apple): "))
#     query = """
#         INSERT INTO product (name, price, description, categories, brand)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     values = (name, price, description, category, brand)
#     cursor.execute(query, values)
#     print(f"Добавленный продукт: {name}, {price}, {description}, {category}, {brand}")
#     print("Новая запись успешно добавлена.")

# def get_update_id(product_id):
#     name = input("Введите название продукта: ")
#     price = float(input("Введите цену продукта: "))
#     description = input("Введите описание продукта: ")
#     category = int(input("Введите ID категории продукта (4 для laptop, 5 для phone, 6 smart watches): "))
#     brand = int(input("Введите ID бренда продукта (26 для Samsung, 27 для Xiaomi, 28 для Apple): "))
#     query = """
#         UPDATE product
#         SET name = %s, price = %s, description = %s, categories = %s, brand = %s
#         WHERE id = %s
#     """
#     values = (name, price, description, category, brand, product_id)
#     cursor.execute(query, values)
#     print(f"Обновленный продукт: {name}, {price}, {description}, {category}, {brand}")
#     print("Запись успешно обновлена.")

# def get_update():
#     product_id = int(input("Введите ID продукта: "))
#     get_product_id(product_id)
#     get_update_id(product_id)

# def all_functions():
#     while True:
#         print('1:  Все продукты')
#         print('2:  Продукт по ID')
#         print('3:  Бренды с продуктами')
#         print('4:  Категории с продуктами')
#         print('5:  Удалить по ID')
#         print('6:  Добавить запись')
#         print('7:  Обновить запись')
#         command = input('Введите команду из выше перечисленных цифрами: ')
#         if not command.isdigit():
#             continue 
#         if command == '1':
#             get_all_product()
#         elif command == "3":
#             brand = input("Введите брэнд: ")
#             print(get_product_brands_by_name(brand))

#         elif command == '4':
#             print("1: Laptops")
#             print("2: Phones")
#             print("3: Smart watches")
#             category = input("Введите категорию: ")
#             if category == '1':
#                 print(get_product_category_laptops())
#             if category == '2':
#                 print(get_product_category_phones())  
#             if category == '3':
#                 print(get_product_category_smartwatches())
#         elif command == '5':
#             get_delete_product_with_id()
#         elif command == '6':
#             get_add_info()
#         elif command == '7':
#             get_update()
#         elif command == '2':
#             get_input_id()
#         answer = input("Хотите ввести другой запрос? 'Y' или выйти? Если выйти то - 'N': ")
#         if answer.lower() == "n":
#             break
#         else:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             continue


# all_functions()


# def all_functions():
#     while True:
#         print('1:  Все продукты')
#         print('2:  Продукт по ID')
#         print('3:  Бренды с продуктами')
#         print('4:  Категории с продуктами')
#         print('5:  Удалить по ID')
#         print('6:  Добавить запись')
#         print('7:  Обновить запись')
#         command = input('Введите команду: ')
#         if command == '1':
#             get_all_product()
#         elif command == "3":
#             print("1: Apple")
#             print("2: Samsung")
#             print("3: Xiaomi")
#             brand = input("Введите брэнд: ")
#             if brand == "1":
#                 print(get_product_brands_apple())
#             elif brand == "2":
#                 print(get_product_brands_samsung())
#             elif brand == "3":
#                 print(get_product_brands_xiaomi())
#         elif command == '4':
#             print("1: Laptops")
#             print("2: Phones")
#             print("3: Smart watches")
#             category = input("Введите категориию: ")
#             if category == '1':
#                 print(get_product_category_laptops())
#             if category == '2':
#                 print(get_product_category_phones())  
#             if category == '3':
#                 print(get_product_category_smartwatches())
#         elif command == '5':
#             get_delete_product_with_id()
#         elif command == '6':
#             get_add_info()
#         elif command == '7':
#             get_update()
#         # elif command == '2':
#         #     print(get_input_id())
#         # answer = input("Хотите ввести другой запрос? 'Y' или 'N': ")
#         # if answer.lower() == "n":
#         #     break
#         # else:
#         #     os.system('cls' if os.name == 'nt' else 'clear')
#         #     continue
#         elif command == '2':
#             try:
#                 print(get_input_id())
#             except Exception as e:
#                 print(f"Ошибка: {e}")
#                 answer = input("Хотите ввести другой запрос? 'Y' или 'N': ")
#                 if answer.lower() == "n":
#                     break

#     else:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         pass
