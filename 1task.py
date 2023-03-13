from globus import *

# _________________________________________________________________________________________________________
# 1 Найдите сколько разных типов продуктов в таблице globus.

# def product_types():
#     query = """
#         SELECT COUNT(DISTINCT product_type_id) FROM globus;
#     """

#     cursor.execute(query=query)
#     r = cursor.fetchone()
#     print('В Глобусе: ', r[0], ' разных типов товара')

# product_types()
# ________________________________________________________________________________________________________
# 2 Используя HAVING найдите сколько и каких продуктов в narodnii испортятся меньше чем через 2 дня.

# def product_dates(): #ошибку выдает что day_to_expire - smallint
#     query = """
#         SELECT COUNT(*) FROM (
#             SELECT product_id,productt_name, day_to_expire, date_delivered,
#             EXTRACT(DAY FROM AGE(NOW(), date_delivered)) AS deliver_time_expire 
#             FROM narodnii
#             GROUP BY product_id
#             HAVIG day_to_expire - EXTRACT(DAY FROM AGE(NOW(), date_delivered)) <= 2)
#         AS ezpired_products_count
#         ;
#     """

#     cursor.execute(query=query)
#     rows = cursor.fetchone()
#     for r in rows:
#         print('Испортятся: ', r)

# product_dates()
# ________________________________________________________________________________________________________
# 3 Посчитайте в каком магазине больше сникерсов в globus или narodnii.

# def find_store_with_most_snickers():
#     query = """
#         SELECT store, SUM(snickers)
#         FROM (
#           SELECT 'globus' AS store, sum(product_amount) AS snickers FROM globus
#           WHERE product_name = 'Snikers'
#           UNION ALL
#           SELECT 'narodnii' AS store, sum(product_amount) AS snickers FROM narodnii
#           WHERE product_name = 'Snikers'
#         ) AS t
#         GROUP BY store
#         ORDER BY SUM(snickers) DESC;
#     """

#     cursor.execute(query)
#     result = cursor.fetchone()
#     print(f"Магазин с наибольшим количеством сникерсов: {result[0]}. Количество сникерсов: {result[1]}")

# find_store_with_most_snickers()
# ________________________________________________________________________________________________________
# 4 Посмотрите продукты в globus и narodnii у которых product_type равен сроку годности продукта.

# def get_products_by_expire_date():
#     query = """
#         SELECT product_id, product_name, product_type_id, day_to_expire
#         FROM globus
#         WHERE product_type_id = day_to_expire
#         UNION ALL
#         SELECT product_id, product_name, product_type_id, day_to_expire
#         FROM narodnii
#         WHERE product_type_id = day_to_expire;
#     """

#     cursor.execute(query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row[0], row[1])

# get_products_by_expire_date()
# ________________________________________________________________________________________________________
# 5 Посмотрите продукты из globus и narodnii у которых одинаковый срок годности.

# def same_day_expire():
#     query = """
#         SELECT g.product_id AS globus_product_id, n.product_id AS narodnii_product_id, g.day_to_expire 
#         FROM globus g 
#         JOIN narodnii n ON g.day_to_expire = n.day_to_expire
#     """

#     cursor.execute(query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row[0], row[1])

# same_day_expire()
# ________________________________________________________________________________________________________
# 6 Через Python подключитесь к БД main и узнайте сколько ВСЕГО piyaz в магазине globus.

# def search_piyaz():
#     query = """
#         SELECT COUNT(*) FROM globus WHERE product_name = 'piyaz'    
#     """

#     cursor.execute(query)
#     result = cursor.fetchone()
#     print(f"Пиазов :{result[0]}")

# search_piyaz()
# ________________________________________________________________________________________________________
# 7 Через Python удалите из магазина narodnii все продукты у которых срок годности 0.

# def delete_day_expire():
#     query = """
#         DELETE FROM narodnii WHERE day_to_expire = 0;    
#     """

#     cursor.execute(query)
#     row_count = cursor.rowcount
#     print(f"Удалено {row_count} продуктов в народном, у кого 0 срок годности")

# delete_day_expire()
# ________________________________________________________________________________________________________
# 8 Если ПРОДУКТ и СРОК ГОДНОСТИ продукта одинаковы в globus и narodnii удалите эту запись из globus.

def delete_from_globus():
    query = """
        DELETE FROM globus
        WHERE EXISTS (
            SELECT *
            FROM narodnii
            WHERE narodnii.product_id = globus.product_id
            AND narodnii.day_to_expire = globus.day_to_expire
        )    
    """

    query = """
        DELETE FROM globus
        WHERE product_id = 16
    """

    cursor.execute(query=query)
    row_count = cursor.rowcount
    print(f"Удалено записей из таблицы globus: {row_count}")

delete_from_globus()