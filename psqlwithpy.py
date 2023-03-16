import psycopg2 
import os 

postgres = psycopg2.connect(
    dbname='my_bot', 
    user='postgres', 
    password='qwerty123', 
    host='localhost',
    port=5432
)

cursor = postgres.cursor()

def get_all_product():
    all_row = """
        SELECT * FROM product
        LIMIT 10;
    """
    cursor.execute(query=all_row)
    all_product = cursor.fetchall()

    return all_product

def get_product_id(prod_id):
    query = """
        SELECT * FROM product
        WHERE id = %s;
        """
    cursor.execute(query, (prod_id,))
    product = cursor.fetchone()
    if product:
        product_date = product[3]
        formated_date = product_date.strftime("%Y-%m-%d %H:%M:%S")
#         print(f"""ID: {product[0]}\nНазвание: {product[6]}\nЦена: {product[1]}\nОписание: {product[2]}
# Дата создания: {product[3]}\nКатегория: {product[4]}\nБрэнд: {product[5]}""")
        return product
    else:
        return None

def get_input_id():
    prod_id = None
    while True:
        # prod_id = input("Введите ID продукта: ")
        if prod_id.isdigit():
            break
        else:
            print("Ошибка! Введите цифры")
    

    get_product_id(prod_id)

# def get_products_by_brand_and_category(brand, category):
#     product_query = """
#     SELECT b.name as brand, COUNT(p.id) as product_count
#     FROM product p
#     JOIN brands b ON p.brand = b.id
#     JOIN category c ON p.categories = c.id
#     WHERE c.name = %s AND b.id = %s
#     GROUP BY b.id, b.name;
#     """
#     cursor.execute(product_query, (brand, category))

#     products = cursor.fetchall()
#     return products

def get_products_by_brand_and_category(brand, category):
    product_query = """
    SELECT p.id, p.name, p.price, c.name as category, b.name as brand
    FROM product p
    JOIN brands b ON p.brand = b.id
    JOIN category c ON p.categories = c.id
    WHERE b.id = %s AND c.name = %s;
    """
    cursor.execute(product_query, (brand, category))

    products = cursor.fetchall()
    return products

def get_products_by_category_and_brand(category, brand):
    product_query = """
        SELECT p.name, p.price, c.name as category, b.name as brand
        FROM product p
        JOIN brands b ON p.brand = b.id
        JOIN category c ON p.categories = c.id
        WHERE c.name = %s AND b.name = %s;
    """
    cursor.execute(product_query, (category, brand))

    products = cursor.fetchall()
    return products

def delete_product_with_id(product_id):
    # product_id = input("Введите ID продукта: ")
    # get_product_id(product_id)
    # answer = input("Удалить запись? Введите 'Yes', чтобы удалить: ")
    # if answer.title() == "yes":
    res = cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    # postgres.commit()
    return 1
    #     print("Запись удалена успешно.")
    # else:
    #     print("Удаление отменено.")

def add_info(name, price, description, category, brand):
    query = """
        INSERT INTO product (name, price, description, categories, brand)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (name, price, description, category, brand)
    cursor.execute(query, values)
    # print(f"Добавленный продукт: {name}, {price}, {description}, {category}, {brand}")
    # print("Новая запись успешно добавлена.")

def update_product_by_id(product_id, name, price, description, category, brand):
    # name = input("Введите название продукта: ")
    # price = float(input("Введите цену продукта: "))
    # description = input("Введите описание продукта: ")
    # category = int(input("Введите ID категории продукта (4 для laptop, 5 для phone, 6 smart watches): "))
    # brand = int(input("Введите ID бренда продукта (26 для Samsung, 27 для Xiaomi, 28 для Apple): "))
    query = """
        UPDATE product
        SET name = %s, price = %s, description = %s, categories = %s, brand = %s
        WHERE id = %s
        """
    values = (name, price, description, category, brand, product_id)
    cursor.execute(query, values)
    # print(f"Обновленный продукт: {name}, {price}, {description}, {category}, {brand}")
    # print("Запись успешно обновлена.")

def update_product():
    product_id = int(input("Введите ID продукта: "))
    print(f"Вы выбрали продукт с ID {product_id}.")
    update_choice = input('Вы хотите изменить продукт? Введите "Y" для подтверждения, иначе введите "N": ')
    if update_choice == "Y":
        update_product_by_id(product_id)
    else:
        print("Отмена изменений.")

def search_products_by_query(query):
    query = query.strip()
    if query.isdigit():
        query = int(query)
        search_query = """
            SELECT *
            FROM product
            WHERE price <= %s
            LIMIT 10
            ;
        """
        cursor.execute(search_query, (query,))
    else:
        search_query = """
            SELECT *
            FROM product
            WHERE name ILIKE %s
            LIMIT 10
            ;
        """
        cursor.execute(search_query, (f"%{query}%",))

    products = cursor.fetchall()
    return products

def all_brands():
    brand = """
        SELECT * FROM brands;
    """
    cursor.execute(query=brand)
    all_brand = cursor.fetchall()

    return all_brand

def all_category():
    category = """
        SELECT * FROM category;
    """
    cursor.execute(query=category)
    all_category = cursor.fetchall()

    return all_category

def get_brand_by_id():
    brand = """
    SELECT id, name FROM brands;
    """
    cursor.execute(query=brand)
    all_brand = cursor.fetchall()

    return all_brand

def get_category_by_id():
    category = """
    SELECT id, name FROM category;
    """
    cursor.execute(query=category)
    all_brand = cursor.fetchall()

    return all_brand

def all_functions():
    while True:
        print('1:  Все продукты')
        print('2:  Продукт по ID')
        print('3:  Бренды с продуктами')
        print('4:  Категории с продуктами')
        print('5:  Удалить по ID')
        print('6:  Добавить запись')
        print('7:  Обновить запись')
        print('8:  Поиск 🔍')
        print('9 : Все бренды')
        print('10: Все категории')
        print('11: Бренд по ID')
        command = input('Введите команду из выше перечисленных цифрами: ')
        if not command.isdigit():
            continue 
        if command == '1':
            get_all_product()
        elif command == "3":
            brand = str(input("Введите бренд. Есть - Apple, Xiaomi, Samsung: "))
            brand = brand.title()
            if not brand.isalpha():
                print("Пожалуйста, введите бренд буквами")
                category = str(input("Введите категорию. Есть - Laptop, Phone, Smart Watches: "))
                category = category.lower()
            elif not brand.isalpha():
                print("Пожалуйста, введите бренд буквами")
            else:
                category = str(input("Введите категорию. Есть - Laptop, Phone, Smart Watches: "))
                category = category.lower()
                if category not in ["laptop", "phone", "smart watches"]:
                    print("Пожалуйста, введите категорию из Laptop, Phone, Smart Watches")
                else:
                    print(get_products_by_brand_and_category(brand, category))
        elif command == '4':
            category = str(input("Введите категорию. Есть - Laptop, Phone, Smart watches : "))
            category = category.lower()
            if category.isdigit():
                print('Пожалуйста, введите категорию буквами')
            else:
                print(get_products_by_category_and_brand(category))
        elif command == '5':
            delete_product_with_id()
        elif command == '6':
            add_info()
        elif command == '7':
            product_id = int(input("Введите ID продукта: "))
            print(f"Вы выбрали изменение продукта с ID \n", get_input_id())
            update_choice = input('\nВы хотите изменить продукт? Введите "Y" для подтверждения, иначе введите "N": ')
            if update_choice.lower() == "y":
                update_product_by_id(product_id)
            else:
                print("Отмена изменений.")

        elif command == '8':
            search = str(input("Введите то что ищете: "))
            search = search.title()
            print(search_products_by_query(search))
        elif command == '9':
            print(all_brands())
        elif command == '10':
            print(all_category())
        elif command == '11':
            print(get_brand_by_id())
        elif command == '12':
            print(get_category_by_id())
        elif command == '2':
            get_input_id()
        answer = input("Хотите ввести другой запрос? 'Y' или выйти? Если выйти то - 'N': ")
        if answer.lower() == "n":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            # cursor.close()
            continue


if __name__ == '__main__':
    all_functions()
