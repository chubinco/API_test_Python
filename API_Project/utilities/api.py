import requests
import json
from loguru import logger
from utilities.http_methods import HttpMethods

base_url = " https://rahulshettyacademy.com"
api_key = "key=qaclick123"


class GoogleMapsApi:
    """ Methods for testing Google Maps API """

    @staticmethod
    def create_new_place():
        """ Create a new location"""

        json_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"
        post_url = f"{base_url}{post_resource}?{api_key}"
        logger.info(f"POST URL: {post_url}")
        response_post = HttpMethods.post(post_url, json_new_place)
        # print(json.dumps(response_post.json(), indent=2))
        return response_post

    @staticmethod
    def get_new_place(place_id):
        """ Method control a new location"""

        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}?{api_key}&place_id={place_id}"
        logger.info(f"GET URL: {get_url}")
        response_get = HttpMethods.get(get_url)
        # print(json.dumps(response_get.json(), indent=2))
        return response_get

    @staticmethod
    def put_new_place(place_id):
        """ Method update a new location"""

        put_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{put_resource}?{api_key}"
        json_update_location = {
            "place_id": place_id,
            "address": "100 Mira street, RU",
            "key": "qaclick123"
        }
        logger.info(f"PUT URL: {put_url}")
        response_put = HttpMethods.put(put_url, json_update_location)
        # print(json.dumps(response_put.json(), indent=2))
        return response_put

    @staticmethod
    def delete_new_place(place_id):
        """ Method delete a new location"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}?{api_key}"
        json_delete_location = {
            "place_id": place_id
        }
        logger.info(f"DELETE URL: {delete_url}")
        response_delete = HttpMethods.delete(delete_url, json_delete_location)
        # print(json.dumps(response_delete.json(), indent=2))
        return response_delete
