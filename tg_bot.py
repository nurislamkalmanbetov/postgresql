from config import TOKEN
import telebot 
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telebot import types
from telebot.types import Message
import psqlwithpy
from psqlwithpy import *


bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(commands=["start"]) # Start
def start_commands(message):
    all_products_button = types.KeyboardButton("/all_prod")
    product_by_id_button = types.KeyboardButton("/product_by_id")
    brands_button = types.KeyboardButton("/brands")
    categories_button = types.KeyboardButton("/categories")
    delete_product_with_id_button = types.KeyboardButton("/delete_with_id")
    add_product_handler_button = types.KeyboardButton("/add_product")
    update_product_handler_button = types.KeyboardButton("/update_product")
    search_product_handler_button = types.KeyboardButton("/search🔍")
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row(all_products_button, product_by_id_button)
    keyboard.row(brands_button, categories_button)
    keyboard.row(delete_product_with_id_button,add_product_handler_button)
    keyboard.row(brands_button, categories_button)
    keyboard.row(update_product_handler_button,search_product_handler_button)
    bot.send_message(message.chat.id, f"Привет! {message.from_user.username}\nИспользуте кнопки, для получения информации", reply_markup=keyboard)


# _____________________________________________________________________________________ All products
@bot.message_handler(commands=["all_prod"])             
def all_products(message):
    product = psqlwithpy.get_all_product()
    for prod in product:
        mess = f'ID: {prod[0]}\n Название: {prod[6]}\n'
        button = telebot.types.InlineKeyboardButton(text='Подробнее', callback_data=f'prod-{prod[0]}')
        # создание клавиатуры
        keyboard = telebot.types.InlineKeyboardMarkup()
        # добавление кнопки в клавиатуру
        keyboard.add(button)
        # отправка сообщения с клавиатурой
        bot.send_message(message.chat.id, mess, reply_markup=keyboard)

# All products's button answer for "Подробнее"
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # если нажали на одну из 36 кнопок — выводим текст
    if call.data.split('-')[0] == 'prod':
        product = psqlwithpy.get_product_id(prod_id=call.data.split('-')[1])
        mess = f'Products\nID: {product[0]}\nНазвание: {product[6]}\nТекст: {product[2]}'
        bot.send_message(call.message.chat.id, mess)
    elif call.data.split('-')[0] == 'brands':
        brands = psqlwithpy.get_brand_by_id(brand_id=call.data.split('-')[1])
        mess = f'Бренд\nID: {brands[0]}\nНазвание: {brands[1]}'
        bot.send_message(call.message.chat.id, mess)
    elif call.data.split('-')[0] == ('category_brand'):
        brand_id = int(call.data.split('-')[1])
        categories = psqlwithpy.all_category()
        for category in categories:
            mess = f'\nНазвание: {category[1]}\n'
            button = telebot.types.InlineKeyboardButton(text='Подробнее', callback_data=f'category-{category[1]}-{brand_id}')
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(button)
            bot.send_message(call.message.chat.id, mess, reply_markup=keyboard)
    elif call.data.startswith('category-'):
        # Handle category button press
        category_name = call.data.split('-')[1]
        brand_id = int(call.data.split('-')[2])
        brands_with_categories = psqlwithpy.get_products_by_brand_and_category(brand_id, category_name)
        for product in brands_with_categories:
            mess = f'Brand: {product[4]}, Product name: {product[1]}, Price: {product[2]}'
            bot.send_message(call.message.chat.id, mess)



    

# _____________________________________________________________________________________Product with id

@bot.message_handler(commands=["product_by_id"])      
def product_by_id(message):
    msg = bot.send_message(message.chat.id, 'Введите ID продукта')
    bot.register_next_step_handler(msg, process_product_by_id_step)

def process_product_by_id_step(message):
    product = psqlwithpy.get_product_id(prod_id=message.text)
    if not product:
        bot.send_message(message.chat.id, 'Продукт с таким ID не найден')
        return
    products_str = f'\nID - {product[0]}\n: Name - {product[6]}\n: Desc - {product[2]}\n: Date - {product[3]}\n: Category - {product[4]}\n: Brand - {product[5]}\n: Price - {product[1]} $\n'
    bot.send_message(message.chat.id, products_str)

# _____________________________________________________________________________________Brands

# Функция вывода списка всех брендов
@bot.message_handler(commands=['brands'])
def all_brands(message):
    brands = psqlwithpy.all_brands()
    for brand in brands:
        mess = f'\nБренд: {brand[1]}\n'
        button = telebot.types.InlineKeyboardButton(text='Категории', callback_data=f'category_brand-{brand[0]}')
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(button)
        bot.send_message(message.chat.id, mess, reply_markup=keyboard)


# _____________________________________________________________________________________ Categories
@bot.message_handler(commands=["categories"])          
def product_category_by_name(message):
    msg = bot.send_message(message.chat.id, 'Введите категорию. Доступны: laptop, phone, smart watches')
    bot.register_next_step_handler(msg, lambda m: process_category_brand_step(m, None, None, None))

def process_category_brand_step(message, name, category, brand):
    category = message.text.lower()
    msg = bot.send_message(message.chat.id, f'Вы выбрали категорию "{category}". Введите бренд. Доступны: Samsung, Xiaomi, Apple:')
    bot.register_next_step_handler(msg, lambda m: process_category_brand_step_2(m, category, brand))

def process_category_brand_step_2(message, category, brand):
    brand = message.text.title()
    products = get_products_by_category_and_brand(category, brand)
    if products:
        products_str = '\n'.join([f'{prod[0]}: {prod[1]}' for prod in products])
        bot.send_message(message.chat.id, f'Продукты категории "{category}" в брендах "{brand}":\n{products_str}')
    else:
        bot.send_message(message.chat.id, f'Нет продуктов категории "{category}" в брендах "{brand}"')



@bot.message_handler(commands=['delete_with_id'])      # Delete_with_id
def delete_product_with_id(message):
    msg = bot.send_message(message.chat.id, 'Введите ID продукта для удаления:')
    bot.register_next_step_handler(msg, process_product_id_step)

def process_product_id_step(message):
    try:
        product_id = int(message.text)
        product = psqlwithpy.get_product_id(product_id)
        if not product:
            bot.send_message(message.chat.id, f'Продукт с ID {product_id} не найден.')
        else:
            products_str = f'\nID - {product[0]}\n: Name - {product[6]}\n: Desc - {product[2]}\n: Date - {product[3]}\n: Category - {product[4]}\n: Brand - {product[5]}\n: Price - {product[1]} $\n'
            msg = bot.send_message(message.chat.id, f'Вы действительно хотите удалить этот продукт? {products_str} (Yes/No)')
            bot.register_next_step_handler(msg, lambda m: process_confirm_deletion_step(m, product_id))
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ID продукта, попробуйте еще раз.')  

def process_confirm_deletion_step(message, product_id):
    if hasattr(message, 'text') and message.text is not None:
        answer = message.text.lower()
        print(answer)
        if answer == 'yes':
            res = psqlwithpy.delete_product_with_id(product_id)
            print('res: ', res)
            if res == 1:
                bot.send_message(message.chat.id, f'Продукт с ID {product_id} удален успешно.')
            else:
                print('Error')
        elif answer.lower() == 'no':
            bot.send_message(message.chat.id, 'Удаление отменено.')
        else:
            bot.send_message(message.chat.id, "Некорректный ответ, введите 'Yes' или 'No'.")
    else:
        bot.send_message(message.chat.id, 'Некорректный тип сообщения, введите текстовое сообщение.')


# ______________________________________________________________________________________ # Add_product


@bot.message_handler(commands=['add_product'])            
def add_product_handler(message):
    msg = bot.send_message(message.chat.id, 'Введите название продукта:')
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    name = message.text
    msg = bot.send_message(message.chat.id, 'Введите описание продукта:')
    bot.register_next_step_handler(msg, lambda m: process_description_step(m, name))

def process_description_step(message, name):
    description = message.text
    msg = bot.send_message(message.chat.id, 'Введите категорию продукта. \n 4 - Laptop, 5 - Phone, 6 - Smart Watches:')
    bot.register_next_step_handler(msg, lambda m: process_category_step(m, name, description))

def process_category_step(message, name, description):
    category = message.text
    msg = bot.send_message(message.chat.id, 'Введите бренд продукта. \n 26 - Samsung, 27 - Xiaomi, 28 - Apple:')
    bot.register_next_step_handler(msg, lambda m: process_brand_step(m, name, description, category))

def process_brand_step(message, name, description, category):
    brand = message.text
    msg = bot.send_message(message.chat.id, 'Введите цену продукта:')
    bot.register_next_step_handler(msg, lambda m: process_price_step(m, name, description, category, brand))

def process_price_step(message, name, description, category, brand):
    try:
        price = float(message.text)
        # Call your function to add the product to the database
        psqlwithpy.add_info(name=name, price=price, description=description, category=category, brand=brand)
        bot.send_message(message.chat.id, f'Продукт "{name}, {price}, {description}, {category}, {brand}" \n успешно добавлен.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректная цена, попробуйте еще раз.')



@bot.message_handler(commands=['update_product'])          # Update
def update_product_handler(message):
    msg = bot.send_message(message.chat.id, 'Введите ID продукта, который вы хотите обновить:')
    bot.register_next_step_handler(msg, process_id_step)

def process_id_step(message):
    try:
        product_id = int(message.text)
        # Check if the product with the given ID exists in the database
        product = psqlwithpy.get_product_id(product_id)
        if product:
            msg = bot.send_message(message.chat.id, f'Вы выбрали запись\n: {product}\n\n \nВведите новое название продукта:')
            bot.register_next_step_handler(msg, lambda m: process_name_step(m, product_id))
        else:
            bot.send_message(message.chat.id, f'Продукт с ID {product_id} не найден.')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ID, попробуйте еще раз.')

def process_name_step(message, product_id):
    name = message.text
    msg = bot.send_message(message.chat.id, 'Введите новое описание продукта:')
    bot.register_next_step_handler(msg, lambda m: process_description_step(m, product_id, name))

def process_description_step(message, product_id, name):
    description = message.text
    msg = bot.send_message(message.chat.id, 'Введите новую категорию продукта. \n 4 - Laptop, 5 - Phone, 6 - Smart Watches:')
    bot.register_next_step_handler(msg, lambda m: process_category_step(m, product_id, name, description))

def process_category_step(message, product_id, name, description):
    category = message.text
    msg = bot.send_message(message.chat.id, 'Введите новый бренд продукта. \n 26 - Samsung, 27 - Xiaomi, 28 - Apple:')
    bot.register_next_step_handler(msg, lambda m: process_brand_step_(m, product_id, name, description, category))

def process_brand_step_(message, product_id, name, description, category):
    brand = int(message.text)
    print(brand)
    msg = bot.send_message(message.chat.id, 'Введите новую цену продукта:')
    bot.register_next_step_handler(msg, lambda m: process_price_step_2(m, product_id, name, description, category, brand))


def process_price_step_2(message, product_id, name, description, category, brand):
    try:
        price = float(message.text)
        # Call your function to update the product in the database
        psqlwithpy.update_product_by_id(product_id=product_id, name=name, price=price,  description=description, category=category, brand=brand)
        bot.send_message(message.chat.id, f'Продукт с ID {product_id} успешно обновлен на " {price}, {description}, {category}, {brand}, {name}".')
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректная цена, попробуйте еще раз.')



@bot.message_handler(commands=['search🔍'])                   # Search
def search_product_handler(message):
    msg = bot.send_message(message.chat.id, 'Введите ключевое слово для поиска:')
    bot.register_next_step_handler(msg, process_search_step)

def process_search_step(message):
    query = message.text.strip()
    matching_products = search_products_by_query(query)
    if not matching_products:
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')
    else:
        for product in matching_products:
            bot.send_message(message.chat.id, f'Название: {product[0]}\nОписание: {product[2]}\nЦена: {product[1]}')



if __name__ == '__main__':
    print('Start bot...')
    bot.infinity_polling()
