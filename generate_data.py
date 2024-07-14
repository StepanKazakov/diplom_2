import random
import string
import requests

from url_data import *


def generate_random_email():
    random_email = ''.join(random.choices(string.ascii_lowercase, k=7))
    return f"{random_email}@yandex.ru"


def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string


def unique_user_data():
    return {
        "email": generate_random_email(),
        "password": generate_random_string(8),
        "name": generate_random_string(6)
    }


def set_random_ingredients():
    # Запрашиваем весь список ингредиентов и сортируем их по видам: булочки, соусы и начинки
    response = requests.get(f"{base_url}{path}/ingredients")
    ingredients_data = response.json()["data"]
    buns = [ingredient["_id"] for ingredient in ingredients_data if ingredient["type"] == "bun"]
    sauces = [ingredient["_id"] for ingredient in ingredients_data if ingredient["type"] == "sauce"]
    mains = [ingredient["_id"] for ingredient in ingredients_data if ingredient["type"] == "main"]

    # Выбираем по одному случайному ингредиенту: булочку, соус и начинку
    selected_bun = random.choice(buns)
    selected_sauce = random.choice(sauces)
    selected_main = random.choice(mains)

    # Возвращаем список хешей для ингредиентов заказа: булочки, соуса и начинки
    return {"ingredients": [selected_bun, selected_sauce, selected_main]}


def set_invalid_ingredients():
    return {"ingredients": [generate_random_string(24), generate_random_string(24), generate_random_string(24)]}
