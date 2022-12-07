import requests


class UsersController:

    def __init__(self):
        self.base_users_path = "https://reqres.in/api/users"

    def get_all_users(self):
        return requests.get(self.base_users_path)

    def get_users_on_page(self, page: int):
        return requests.get(self.base_users_path, params={"page": page})
