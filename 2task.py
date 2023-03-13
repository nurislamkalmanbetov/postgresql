from globus import *

# _____________________________________________________________________________________________________
# 9 Напишите запрос, который выводит всю информацию продукта из народного,
# где количество продуктов 200 < продукт < 1001

# def prod_amunt():
#     query = """
#         SELECT * FROM narodnii
#         WHERE product_amount > 200 AND product_amount < 1001;
#     """
#     cursor.execute(query)
#     result = cursor.fetchall()
#     print(f"Все записи из народного по запросу: {result}")

# prod_amunt()
# _____________________________________________________________________________________________________
# 10 Напишите запрос, который соединяет таблицы глобус народный и выводит day delivered

# def join_dates():
#     query = """
#         SELECT g.*, n.*
#         FROM globus g
#         JOIN narodnii n ON g.product_id = n.product_id;    
#     """

#     cursor.execute(query)
#     results = cursor.fetchall()

#     for row in results:
#         print(row)

# join_dates()

# _____________________________________________________________________________________________________
# 11 Напишите запрос, который соединяет таблицы глобус народный по столбцу глобуса и выводит название продукта

# def join_by_name():
#     query = """
#         SELECT g.product_name
#         FROM globus g
#         LEFT JOIN narodnii n ON g.product_name = n.product_name
#     """

#     cursor.execute(query)
#     result = cursor.fetchall()
#     print(f"Названия продуктов в глобусе и народном: {result}")

# join_by_name()

# _____________________________________________________________________________________________________
# 12 Напишите запрос, который соединяет таблицы глобус народный
# по столбцу Hародного и выводит название продукта
 
# def join_products_narodnii():
#     query = """
#         SELECT n.product_name
#         FROM narodnii n
#         RIGHT JOIN globus g ON n.product_id = g.product_id;
#     """
#     cursor.execute(query)
#     result = cursor.fetchall()
#     print('Название продуктов, совпадающих в народном и глобусе:', result) - почему не в {}? потому чт str


# join_products_narodnii()

# _____________________________________________________________________________________________________
# 13 - такая же задача как и 11 вверху!
# 
# _____________________________________________________________________________________________________
# 14 Напишите запрос, который соединяет таблицы глобус народный
# и выводит совпадения количества продуктов.

# def join_product_quantities():
#     query = """
#         SELECT g.product_id, g.product_amount, n.product_amount
#         FROM globus g
#         INNER JOIN narodnii n ON g.product_id = n.product_id
#         WHERE g.product_amount = n.product_amount
#     """

#     cursor.execute(query)
#     result = cursor.fetchall()
#     print(f'Совпадения количества продуктов:', [result])

# join_product_quantities()

# _____________________________________________________________________________________________________
# 15 Напишите запрос, который выводит продукты глобуса, где название заканчивается на a, b, c, d, e, f, g, a

# def globus_products():
#     query = """
#         SELECT *
#         FROM globus
#         WHERE product_name LIKE '%a' OR
#               product_name LIKE '%b' OR
#               product_name LIKE '%c' OR
#               product_name LIKE '%d' OR
#               product_name LIKE '%e' OR
#               product_name LIKE '%f' OR
#               product_name LIKE '%g' OR
#               product_name LIKE '%h';
#     """
#     cursor.execute(query)
#     result = cursor.fetchall()
#     print("Продукты глобуса, где название заканчивается на a, b, c, d, e, f, g, h:")
#     for row in result:
#         print(row)

# globus_products()















