import allure
from base_methods import BaseMethods


class ApiUser(BaseMethods):
    def __init__(self):
        super().__init__()

    @allure.step("Создание пользователя: {payload}")
    def create_user(self, payload):
        return self.post("/auth/register", payload)

    @allure.step("Логин пользователя: {payload}")
    def login_user(self, payload):
        return self.post("/auth/login", payload)

    @allure.step("Изменение данных пользователя: {payload}")
    def update_user(self, payload, headers):
        return self.patch("/auth/user", payload, headers=headers)
