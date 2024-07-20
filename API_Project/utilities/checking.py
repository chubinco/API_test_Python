import json
from loguru import logger


class Checking:
    """ Methods checking our response """

    @staticmethod
    def check_status_code(response, status_code):
        """ Method checking status code"""
        assert response.status_code == status_code, f"Failed!!! Status Code: {response.status_code}"
        logger.info(f"Success!!! Status Code: <{response.status_code}>")

    @staticmethod
    def check_json_fields(response, expected_value):
        """ Method for checking required fields in the response of request """
        fields = json.loads(response.text)
        assert list(fields.keys()) == expected_value, (
            f"Fields verification is wrong"
        )
        logger.info(f"All keys of fields verified!")

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """ Method for checking the values of required fields in the response of request """
        field_value = response.json().get(field_name)
        # print(field_value)
        assert field_value == expected_value, f"The value <{field_name}>: <{field_value}> is wrong"
        logger.info(f"The value <{field_name}>: <{field_value}> is correct")

    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        """ Method for checking the values of required fields in the response of request for a given word """
        field_value = response.json().get(field_name)
        assert search_word in field_value, (
            f"Word: <{search_word}> not in field of response <{field_name}>")
        logger.info(
            f"Word: <{search_word}> found in field of response <{field_name}>")
