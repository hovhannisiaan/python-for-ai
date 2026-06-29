from idlelib.rpc import request_queue

import requests
from urllib3 import _request_methods


# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts/1"
# )

# if response.status_code == 200:
#     print("Success")
# else:
#     print("Request failed")
#     print(response.status_code)
# url = "https://jsonplaceholder.typicode.com/posts"



# try:
#     response = requests.get(url, timeout=5)
#     data = response.json()

#     if response.status_code == 200:
#         print(data[0]["title"])
#     else: 
#         print(f"HTTP error code: {response.status_code}")

# except requests.Timeout:
#     print("the request timeout")

# except requests.ConnectionError:
#     print("Could not connect to the server.")

# except requests.RequestException as e:
#     print(e)

# try: 
#     response = requests.get(url, timeout=5)
#     response.raise_for_status()
#     data = response.json()
#     print(data)
#     print(response.status_code)

# except requests.HTTPError as e:
#     print(e)

class JsonPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.timeout = 5
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
        })

    def _request(self, method, endpoint, **kwargs):
        try:
            response = self.session.request(
                method,
                f"{self.base_url}/{endpoint}",
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            return response.json()

        except requests.Timeout:
            print("Request timed out.")
            return None

        except requests.ConnectionError:
            print("Connection failed.")
            return None

        except requests.HTTPError as e:
            print(e)
            return None

        except requests.RequestException as e:
            print(e)
            return None

    def get_users(self):
        return self._request(method="GET", endpoint="users")

    def get_user_by_id(self, user_id):
        return self._request(method="GET", endpoint=f"users/{user_id}")

    def get_posts(self):
        return self._request(method="GET", endpoint="posts")

    def get_post_by_id(self, post_id):
        return self._request(method="GET", endpoint=f"posts/{post_id}")

    def create_post(self, title, body, user_id):
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        return self._request(
            method="POST",
            endpoint="posts",
            json=data
        )

    def update_post(self, post_id, title, body, user_id):
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        return self._request(
            method="PUT",
            endpoint=f"posts/{post_id}",
            json=data
        )

    def patch_post(self, post_id, **kwargs):

        return self._request(
            method="PATCH",
            endpoint=f"posts/{post_id}",
            json=kwargs
        )

    def delete_post(self, post_id):
        return self._request(
            method="DELETE",
            endpoint=f"posts/{post_id}"
        )

    def close(self):
        self.session.close()

posts = JsonPlaceholderClient()

try:
    print(posts.get_post_by_id(6))
finally:
    posts.close()