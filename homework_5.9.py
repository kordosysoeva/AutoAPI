import requests

class Test_new_location_1():
    """Работа с новой локацией"""

    def test_create_new_location(self):

        """Создание новых пяти локаций """
        iteration_for_put = 0
        while iteration_for_put < 5:
            base_url = "https://rahulshettyacademy.com"
            key = "?key=qaclick123"     # params for all requests
            post_resource = "/maps/api/place/add/json"  # post resource
            post_url = base_url + post_resource + key
            print(post_url)
            json_for_create_new_location = {"location": {"lat": -38.383494,"lng": 33.427362}, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park","shop"],
                "website": "http://google.com",
                "language": "French-IN" }

            result_post = requests.post(post_url, json=json_for_create_new_location)
            json_post = result_post.json()

            """Вытаскиваем place_id и помещаем в текстовый файл"""
            value_for_db = json_post.get('place_id')
            print(value_for_db)
            if iteration_for_put == 0:
                with open("C:\\Users\\Kristina\\PycharmProjects\\AutoAPI_git\\DB_place_id", 'w') as file:
                    write_value = file.write(str(value_for_db) + "\n")

            else:
                with open("C:\\Users\\Kristina\\PycharmProjects\\AutoAPI_git\\DB_place_id", 'a') as file:
                    write_value = file.write(str(value_for_db) + "\n")
            iteration_for_put += 1

        """Проверка создания новых пяти локаций"""
        get_resource = "/maps/api/place/get/json"
        with open("C:\\Users\\Kristina\\PycharmProjects\\AutoAPI_git\\DB_place_id", 'r') as file:
            for line in file.readlines(): # Цикл для построчного чтения файла
                print(line.rstrip('\n\r'))
                get_url = base_url + get_resource + key + "&place_id=" + line.rstrip('\n\r')
                print(get_url)
                result_get = requests.get(get_url)
                print(result_get.text)
                print("Статус код: " + str(result_get.status_code))
                assert 200 == result_get.status_code
                print('==================================================================' + "\n")

new_place = Test_new_location_1()
new_place.test_create_new_location()
