class UsersFilter:
    def __init__(self, users):
        self.users = users

    def get_users_in_range(self, start_id, end_id):
        filtered_users = [user for user in self.users if start_id <= user['id'] <= end_id]

        sorted_users = sorted(filtered_users, key=lambda users: users['first_name'])

        return [f"{user['first_name']} {user['last_name']}" for user in sorted_users]
