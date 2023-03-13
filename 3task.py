import psycopg2
import random as rd

# bd_password = input("Введите пароль от Базы Данных: ")
# 1
postgres = psycopg2.connect(
    dbname='market', 
    user='postgres', 
    password='postgres', 
    host='localhost',
    port=5432
)

cursor = postgres.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS sizes (
#         id SERIAL PRIMARY KEY,
#         foot_size INTEGER NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
# """)

# postgres.commit()

# Закрытие соединения
# _________________________________________________________________________________________________
# 2 Создайте вторую таблицу которая хранит в себе id из таблицы sizes
# и имя человека с помощью INNER JOIN выведите на экран Имя человека и размер его обуви.

# cursor.execute("""
#     CREATE TABLE people (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         size_id INTEGER NOT NULL,
#         FOREIGN KEY (size_id) REFERENCES sizes (id)
#     );
# """)

# postgres.commit()
# Вставка данных в таблицу sizes
# cursor.execute("""
#     INSERT INTO sizes (foot_size) VALUES (42);
#     INSERT INTO sizes (foot_size) VALUES (39);
#     INSERT INTO sizes (foot_size) VALUES (45);
# """)
# cursor.execute("""
#     INSERT INTO people (name, size_id) VALUES ('test', 6);
#     INSERT INTO people (name, size_id) VALUES ('nick', 5);
#     INSERT INTO people (name, size_id) VALUES ('poll', 5);
# """)

# postgres.commit()


cursor.execute("""
    SELECT people.name, sizes.foot_size
    FROM sizes 
    INNER JOIN people ON people.size_id = sizes.id
""")



cursor.close()
postgres.close()