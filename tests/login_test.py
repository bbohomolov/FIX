import allure
import requests
import pytest
from my_utils import MyUtils


param_list = [
        ({"email": "peter@klaven", "password": "cityslicka"}, requests.codes.ok, "token"),
        ({"password": "cityslicka"}, requests.codes.bad, "error"),
        ({"email": "peter@klaven"}, requests.codes.bad, "error"),
        ({"email":"1", "password": "1"}, requests.codes.not_found, "error"),
        ({}, requests.codes.bad, "error"),
        ]

ids_list = ["successful","w/o email","w/o password","invalid email/password","w/o parameters"]
u = MyUtils()


@pytest.fixture(scope='function', params=param_list, ids=ids_list)
def param_test(request):
    return request.param


class TestClass():

    login_request = "api/login"
    email = "peter@klaven"
    password = "cityslicka"

    @allure.feature("Login")
    @allure.testcase("Login")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login(self, param_test):
        (data, code, expected_response) = param_test
        r = u.send_post_request(self.login_request, data)
        u.attach_response(r.text)
        u.attach_sent_url(r.url+str(data))
        u.check_response_status(r.status_code, code)
        u.check_response_body(r.text, expected_response)
