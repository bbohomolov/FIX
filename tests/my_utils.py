import allure
import requests
from allure.constants import AttachmentType


class MyUtils():

    url = "https://reqres.in/"

    @allure.step("Check response status.")
    def check_response_status(self, actual, expected):
        assert actual == expected, "Received response " + str(actual) + " status doesn't equal " + str(expected)

    @allure.step("Check response body.")
    def check_response_body(self, actual, expected):
        if expected in actual:
            assert True
        else:
            assert False, "Response body doesn't contain " + expected

    @allure.step("Received response.")
    def attach_response(self, text):
        allure.attach('Received response', text, AttachmentType.JSON)

    @allure.step("Sent URL.")
    def attach_sent_url(self, text):
        allure.attach('Sent URL', text, AttachmentType.TEXT)

    @allure.step("Send POST request.")
    def send_post_request(self, url, data):
        return requests.post(self.url + url, data)