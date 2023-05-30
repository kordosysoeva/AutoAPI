import requests

class Test_new_joke():
    """Create new joke!"""

    def __init__(self):
        pass

    def get_list_category(self):
        """Get list category"""
        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        print("Status code is " + str(result.status_code))
        assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
        result.encoding = 'utf-8'
        self.list_category = result.json()
        print(self.list_category)
        print("\033[32mPASSED\n==========================================================\033[0m")


    def test_create_new_joke_for_all_categories(self):
        """Create massive joke for all categories"""
        categories = self.list_category
        for category in categories:
            url = "https://api.chucknorris.io/jokes/random?category=" + category
            print(url)
            result = requests.get(url)
            print("Status code is " + str(result.status_code))
            assert 200 == result.status_code, "Провал!!! Запрос ошибочный"
            result.encoding = 'utf-8'
            print("Request is " + str(result.json()))
            check = result.json()

            """Assert value""" #Checking that the name Chuck is mentioned at least once in a joke

            check_info_value = check.get("value")
            print(check_info_value)
            name = "Chuck"
            if name in check_info_value:
                print("Chuck here!")
            else:
                print("Chuck lost!")
            print("\033[32mPASSED\n==========================================================\033[0m")


random_joke = Test_new_joke()
random_joke.get_list_category()
random_joke.test_create_new_joke_for_all_categories()
