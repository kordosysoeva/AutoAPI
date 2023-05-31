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
        check_msg = check_get_info.get('address')
        print("Address is " + check_msg)
        assert check_msg == "100  D8FdDF Lenina street, RU", "Sad"
        print("Address is ok!")

        """Удаление локации - 200"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {"place_id": place_id}
        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)
        assert 200 == result_delete.status_code, "Sad"
        print("Status code is " + str(result_delete.status_code))
        check_delete_info = result_delete.json()
        check_status = check_delete_info.get('status')
        print("Status is " + check_status)
        assert check_status == "OK", "Sad"
        print("Status is OK!")

        """Удаление локации - 404"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {"place_id": 5555}
        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)
        assert 404 == result_delete.status_code, "Sad"
        print("Status code is " + str(result_delete.status_code))
        check_delete_info = result_delete.json()
        check_delete_msg = check_delete_info.get('msg')
        print("Message: " + check_delete_msg)
        assert check_delete_msg == "Delete operation failed, looks like the data doesn't exists", "Sad"
        print("Message is ok!")

        """Проверка удаления новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        assert 404 == result_get.status_code
        print("Status code is " + str(result_get.status_code))
        check_get_info = result_get.json()
        check_msg = check_get_info.get('msg')
        print("Message is " + check_msg)
        assert check_msg == "Get operation failed, looks like place_id  doesn't exists", "Sad"
        print("Message is ok!")

        print("Тестирование test_new_location PASSED5")

new_place = Test_new_location()
new_place.test_create_new_location()