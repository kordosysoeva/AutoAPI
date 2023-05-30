import requests

class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):

        """Create new location"""

        base_url = "https://rahulshettyacademy.com"     # base url
        key = "?key=qaclick123"     # params for all requests
        post_resource = "/maps/api/place/add/json"  # post resource
        post_url = base_url + post_resource + key
        print(post_url)
        json_for_create_new_location = {"location": {
            "lat": -38.383494,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
             "shoe park",
            "shop"
             ],
             "website": "http://google.com",
            "language": "French-IN"
            }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        assert 200 == result_post.status_code
        print("Status code is " + str(result_post.status_code))

        """Assert status"""
        check_post_status = result_post.json().get("status")
        print("Status response is " + check_post_status)
        assert check_post_status == "OK"
        print("Status is OK!")

        place_id = result_post.json().get("place_id")
        print("Place id is " + place_id)

        """Check create new location"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + str(place_id)
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        assert 200 == result_get.status_code
        print("Status code is " + str(result_get.status_code))


        """Изменение новой локации - 200"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {
            "place_id": place_id,
            "address": "100  D8FdDF Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_location)
        print(result_put.text)
        assert 200 == result_put.status_code, "Sad"
        print("Status code is " + str(result_put.status_code))
        check_put_info = result_put.json()
        check_msg = check_put_info.get('msg')
        print("Message is " + check_msg)
        assert check_msg == "Address successfully updated", "Sad"
        print("Message is ok!")

        """Изменение новой локации - 404"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {
            "place_id": 556,
            "address": "100  D8FdDF Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_location)
        print(result_put.text)
        assert 404 == result_put.status_code, "Sad"
        print("Status code is " + str(result_put.status_code))
        check_put_info = result_put.json()
        check_msg = check_put_info.get('msg')
        print("Message is " + check_msg)
        assert check_msg == "Update address operation failed, looks like the data doesn't exists", "Sad"
        print("Message is ok!")

        """Проверка изменения новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code
        print("Status code is " + str(result_get.status_code))
        check_get_info = result_get.json()
        check_address = check_get_info.get('address')
        print("Address is " + check_address)
        assert check_address == "100  D8FdDF Lenina street, RU", "Sad"
        print("Address is ok!")

new_place = Test_new_location()
new_place.test_create_new_location()