import allure
from api_methods.api_order import ApiOrder
from generate_data import set_invalid_ingredients, set_random_ingredients
from response_data import *


@allure.feature("Order API")
class TestOrder:
    @classmethod
    def setup_class(cls):
        cls.api_order = ApiOrder()

    @allure.title("Создание заказа с ингредиентами и авторизацией")
    def test_create_order_with_authorization(self, set_header):
        order_data = set_random_ingredients()
        with allure.step("Создание заказа с ингредиентами и авторизацией"):
            response = self.api_order.create_order(order_data, set_header)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа с ингредиентами без авторизации")
    def test_create_order_without_authorization(self):
        order_data = set_random_ingredients()
        with allure.step("Создание заказа с ингредиентами без авторизации"):
            response = self.api_order.create_order(order_data)
        assert response.status_code == 200
        assert response.json().get("success") == True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        order_data = {"ingredients": []}
        with allure.step("Создание заказа без ингредиентов"):
            response = self.api_order.create_order(order_data)
        assert response.status_code == 400
        assert response.json().get("message") == miss_ingredient

    @allure.title("Создание заказа из несуществующих ингредиентов")
    def test_create_order_with_invalid_ingredients(self):
        order_data = set_invalid_ingredients()
        with allure.step("Создание заказа из несуществующих ингредиентов"):
            response = self.api_order.create_order(order_data)
        assert response.status_code == 500

    @allure.title("Получение заказов конкретного пользователя с авторизацией")
    def test_get_orders_authorized(self, set_header):
        with allure.step("Получение заказов конкретного пользователя с авторизацией"):
            response = self.api_order.get_orders(set_header)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказов конкретного пользователя без авторизации")
    def test_get_orders_unauthorized(self):
        with allure.step("Получение заказов конкретного пользователя без авторизации"):
            response = self.api_order.get_orders()
        assert response.status_code == 401
        assert response.json().get("message") == unauthorised
