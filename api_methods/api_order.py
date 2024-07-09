import allure
from base_methods import BaseMethods


class ApiOrder(BaseMethods):
    def __init__(self):
        super().__init__()

    @allure.step("Create an order with payload: {payload}")
    def create_order(self, payload, headers=None):
        return self.post("/orders", payload, headers)

    @allure.step("Get orders")
    def get_orders(self, headers=None):
        return self.get_data("/orders", headers)
