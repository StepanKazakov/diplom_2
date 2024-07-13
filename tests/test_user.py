import pytest
import allure
from api_methods.api_user import ApiUser
from generate_data import unique_user_data, user_missing_name, user_missing_password, user_missing_email
from response_data import *


@allure.feature("User API")
class TestUser:
    @classmethod
    def setup_class(cls):
        cls.api_user = ApiUser()

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self):
        new_user = unique_user_data()
        with allure.step("Создание уникального пользователя"):
            response = self.api_user.create_user(new_user)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        new_user = unique_user_data()
        with allure.step("Создание пользователя, который уже зарегистрирован"):
            self.api_user.create_user(new_user)
            response = self.api_user.create_user(new_user)
        assert response.status_code == 403
        assert response.json().get("message") == duplicate_user

    @pytest.mark.parametrize("user_data", [user_missing_email, user_missing_password, user_missing_name])
    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    def test_create_user_missing_field(self, user_data):
        user_data = user_data()
        with allure.step("Создание трех пользователей, у каждого нет одного из трех обязательных полей"):
            response = self.api_user.create_user(user_data)
        assert response.status_code == 403
        assert response.json().get("message") == required_fields

    @allure.title("Логин под существующим пользователем")
    def test_login_user(self):
        new_user = unique_user_data()
        with allure.step("Регистрируем пользователем"):
            self.api_user.create_user(new_user)
        with allure.step("Логинимся под существующим пользователем"):
            response = self.api_user.login_user(new_user)
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Логин с рандомными логином и паролем")
    def test_login_user_wrong_credentials(self):
        new_user = unique_user_data()
        with allure.step("Логин с рандомными логином и паролем без регистрации пользователя"):
            response = self.api_user.login_user(new_user)
        assert response.status_code == 401
        assert response.json().get("message") == incorrect_credentials

    @allure.title("Изменение данных авторизованного пользователя")
    def test_update_user_with_authorization(self, set_header):
        with allure.step("Изменяем данные авторизованного пользователя"):
            update_data = {"name": "New Name"}
            response = self.api_user.update_user(update_data, headers=set_header)
        assert response.status_code == 200
        assert response.json().get("user").get("name") == "New Name"

    @allure.title("Изменение данных не авторизованного пользователя")
    def test_update_user_without_authorization(self):
        update_data = {"name": "New Name"}
        with allure.step("Изменение данных не авторизованного пользователя"):
            response = self.api_user.update_user(update_data, {})
        assert response.status_code == 401
        assert response.json().get("message") == unauthorised
