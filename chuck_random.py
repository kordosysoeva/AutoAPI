import requests

class Test_new_joke():
    """Create new joke!"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Create random joke"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Status code is " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        """Assert categories"""

        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Category passed")

        """Assert value"""

        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck here!")
        else:
            print("Chuck lost")

    def test_create_new_random_category_joke(self):
        """Create random joke on a specific topic"""
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status code is " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        """Assert categories"""

        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Category passed")

        """Assert value"""

        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck here!")
        else:
            print("Chuck lost")

    def test_create_new_random_category_joke_negative(self):
        """Create random joke on a specific topic whith empty categories"""
        category = "empty_cat"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status code is " + str(result.status_code))
        assert 404 == result.status_code, "Провал!!! Запрос ошибочный"
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        """Assert status"""

        check_info = check.get("status")
        print(check_info)
        assert check_info == 404
        print("Status passed")

        """Assert error"""

        check_info_error = check.get("error")
        print(check_info_error)
        name = "Not Found"
        if name in check_info_error:
            print("Error here!")
        else:
            print("Another error")

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()

print("===============================================================")
sport_joke = Test_new_joke()
sport_joke.test_create_new_random_category_joke()

print("===============================================================")
negative_test = Test_new_joke()
negative_test.test_create_new_random_category_joke_negative()
