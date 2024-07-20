import json
from datetime import datetime
from pathlib import Path

import allure
from requests import Response
from loguru import logger
from utilities.checking import Checking
from utilities.api import GoogleMapsApi


@allure.epic("Test create new location")
class TestCreatePlace:
    """ Testing of methods for creating, updating and deleting objects using API Google Maps """

    @allure.description("Testing create, update and delete new location")
    def test_create_new_place(self):
        """ Test creating a new place """
        root = Path(__file__).resolve().parent.parent
        time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logger.add(root.joinpath('logs', f'file_{time_now}.log'),
                   rotation="1 week")

        logger.info(f"\n=== Method POST ===")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json().get("place_id")  # get place_id
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post,
                                   ['status', 'place_id', 'scope', 'reference',
                                 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        logger.info(f"\n=== Method GET after post ===")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name',
                                 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Checking.check_json_value(result_get, 'address',
                                  '29, side layout, cohen 09')

        logger.info(f"\n=== Method PUT ===")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg',
                                  'Address successfully updated')

        logger.info(f"\n=== Method GET after put ===")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name',
                                 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Checking.check_json_value(result_get, 'address', '100 Mira street, RU')

        logger.info(f"\n=== Method DELETE ===")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        logger.info(f"\n=== Method GET after delete ===")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg',
                                  "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        logger.info(
            f"Testing of methods for creating, updating and deleting objects using API Google Maps has been successfully completed")
