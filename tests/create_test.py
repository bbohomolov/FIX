import allure
import requests
import pytest
from my_utils import MyUtils


param_list = [
        ({"name": "morpheus","job": "leader"}, requests.codes.created, ""),
        ({"name": "morpheus","job": "leader"}, requests.codes.bad, ""),
        ({"job": "leader"}, requests.codes.bad, ""),
        ({"name": "morpheus"}, requests.codes.bad, ""),
        ({}, requests.codes.bad, "error"),
        ]

ids_list = ["successful","existent user","w/o name","w/o job","w/o parameters"]
u = MyUtils()


@pytest.fixture(scope='function', params=param_list, ids=ids_list)
def param_test(request):
    return request.param


class TestClass():

    create_request = "api/users/"
    email = "peter@klaven"
    password = "cityslicka"

    @allure.feature("Create")
    @allure.testcase("Create")
    @allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_create(self, param_test):
        (data, code, expected_response) = param_test
        r = u.send_post_request(self.create_request, data)
        u.attach_response(r.text)
        u.attach_sent_url(r.url+str(data))
        u.check_response_status(r.status_code, code)
        u.check_response_body(r.text, expected_response)
