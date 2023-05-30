import requests

class Test_new_joke():
    """Create new joke!"""

    def __init__(self):
        pass

    def message_for_user(self):
        print("Hi! Do you wanna joke? Input category and wait!")
        self.category = input()


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

        while self.category not in self.list_category:
            print("\033[31mYou selected incorrect category! Try again\033[0m")
            self.category = input()
            break
        print("\033[32mPASSED\n==========================================================\033[0m")


    def test_create_new_joke_from_request_user(self):
        """Create  joke for user category"""

        url = "https://api.chucknorris.io/jokes/random?category=" + self.category
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
random_joke.message_for_user()
random_joke.get_list_category()
random_joke.test_create_new_joke_from_request_user()

