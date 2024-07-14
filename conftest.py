import pytest
from api_methods.api_user import ApiUser
from generate_data import unique_user_data


@pytest.fixture(scope='session')
def set_header():
    api_user = ApiUser()
    user_data = unique_user_data()
    response = api_user.create_user(user_data)
    return {"Authorization": response.json()["accessToken"]}
