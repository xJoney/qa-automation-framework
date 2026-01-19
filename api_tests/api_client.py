import requests

class ReqresAPI:
    
    def get_users(self, page=1):
        return requests.get(f"https://dummyjson.com/users")

    def get_user(self, user_id):
        return requests.get(f"https://dummyjson.com/users/{user_id}")

    def create_user(self, payload):
        return requests.post(f"https://dummyjson.com/users/add", json=payload)

    def update_user(self, user_id, payload):
        return requests.put(f"https://dummyjson.com/users/{user_id}", json=payload)
