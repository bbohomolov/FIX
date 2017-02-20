import allure
import requests
import pytest
from my_utils import MyUtils

u = MyUtils()
param_list = [
        ("peter@klaven", "!@^&#%&*"),
        ("peter@klaven", "1"),
        ("!@^&#%&*", "cityslicka"),
        ("1", "cityslicka")
        ]
ids_list = ["symbolic pass", "short pass", "symbolic email", "short email"]


@pytest.fixture(scope='function', params=param_list, ids=ids_list)
def param_test(request):
    return request.param


class TestClass():

    email = "newpeter@klaven"
    password = "newcityslicka"
    register_request = "api/register"

    @allure.feature("Register")
    @allure.testcase("Positive: Register test")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_register(self):
        r = u.send_post_request(self.register_request, {'email': self.email, 'password': self.password})
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.created)
        u.check_response_body(r.text, "token")

    @allure.feature("Register")
    @allure.testcase("Negative: Register test no password")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_register_negative_nopasswd(self):
        r = u.send_post_request(self.register_request, {'email': self.email})
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")

    @allure.feature("Register")
    @allure.testcase("Negative: Register test no email")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_register_negative_noemail(self):
        r = u.send_post_request(self.register_request, {'password': self.password})
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")

    @allure.feature("Register")
    @allure.testcase("Negative: Register test email/password check")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_register_negative(self, param_test):
        (email, password) = param_test
        r = u.send_post_request(self.register_request, {'email': email, 'password': password})
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")