import allure
import requests
import pytest
from my_utils import MyUtils

param_list = [
        ("peter@klaven", "abcdefg"),
        ("peter@klaven", "!@^&#%&*"),
        ("peter@klaven", "1"),
        ("peter", "cityslicka"),
        ("!@^&#%&*", "cityslicka"),
        ("1", "cityslicka")
        ]
ids_list = ["incorrect pass", "symbolic pass", "short pass", " incorrect email", "symbolic email", "short email"]
u = MyUtils()


@pytest.fixture(scope='function', params=param_list, ids=ids_list)
def param_test(request):
    return request.param


class TestClass():

    login_request = "api/login"
    email = "peter@klaven"
    password = "cityslicka"

    @allure.feature("Login")
    @allure.testcase("Positive: Login test")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login(self):
        r = u.send_post_request(self.login_request, {'email': self.email, 'password': self.password})
        u.attach_response(r.text)
        u.attach_sent_URL(r.url)
        u.check_response_status(r.status_code, requests.codes.ok)
        u.check_response_body(r.text, "token")

    @allure.feature("Login")
    @allure.testcase("Negative: Login test no password")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login_negative_nopasswd(self):
        r = u.send_post_request(self.login_request, {'email': self.email})
        u.attach_response(r.text)
        u.attach_sent_URL(r.url)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")

    @allure.feature("Login")
    @allure.testcase("Negative: Login test no email")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login_negative_noemail(self):
        r = u.send_post_request(self.login_request, {'password': self.password})
        u.attach_response(r.text)
        u.attach_sent_URL(r.url)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")

    @allure.feature("Login")
    @allure.testcase("Negative: Login test email/password check")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login_negative(self, param_test):
        (email, password) = param_test
        r = u.send_post_request(self.login_request, {'email': email, 'password': password})
        u.attach_response(r.text)
        u.attach_sent_URL(r.url)
        u.check_response_status(r.status_code, requests.codes.bad)
        u.check_response_body(r.text, "error")
