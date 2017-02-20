import allure
import requests
import pytest
from my_utils import MyUtils

u = MyUtils()


class TestClass():

    email = "newpeter@klaven"
    password = "newcityslicka"
    single_user_request = "api/users/"
    user_id = "2"
    nonexistent_user_id = "999999"

    @allure.feature("Single User")
    @allure.testcase("Positive: Single User test")
    @allure.severity(pytest.allure.severity_level.MINOR)
    def test_single_user(self):
        r = u.send_get_request(self.single_user_request+self.user_id)
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.ok)
        u.check_response_body(r.text, self.user_id)

    @allure.feature("Single User")
    @allure.testcase("Negative: Single User test")
    @allure.severity(pytest.allure.severity_level.MINOR)
    def test_single_user_negative(self):
        r = u.send_get_request(self.single_user_request+self.nonexistent_user_id)
        u.attach_sent_URL(r.url)
        u.attach_response(r.text)
        u.check_response_status(r.status_code, requests.codes.not_found)
        u.check_response_body(r.text, "")
