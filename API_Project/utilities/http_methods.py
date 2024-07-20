import allure
import requests
import json
from loguru import logger


class HttpMethods:
    """ List http methods """

    headers = {'Content-Type': 'application/json'}
    cookie =""

    @staticmethod
    def get(url):
        with allure.step("GET request"):
            logger.info(f"GET request: {url}")
            response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            logger.info(f"{response}")
            return response

    @staticmethod
    def post(url, body):
        with allure.step("POST request"):
            logger.info(f"POST request: {url}")
            response = requests.post(url, headers=HttpMethods.headers, json=body, cookies=HttpMethods.cookie)
            logger.info(f"{response}")
            return response

    @staticmethod
    def put(url, body):
        with allure.step("PUT request"):
            logger.info(f"PUT request: {url}")
            response = requests.put(url, headers=HttpMethods.headers, json=body, cookies=HttpMethods.cookie)
            logger.info(f"{response}")
            return response

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE request"):
            logger.info(f"Delete request: {url}")
            response = requests.delete(url, headers=HttpMethods.headers, json=body, cookies=HttpMethods.cookie)
            logger.info(f"{response}")
            return response

