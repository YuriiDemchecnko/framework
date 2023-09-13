import requests
import json


class ThinkingTester:
    def __init__(self) -> None:
        # The URL of the API's login endpoint
        login_url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

        # User credentials
        payload = {"email": "d1@example.com", "password": "1234567"}

        try:
            # Send the POST request
            response = requests.post(
                login_url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            )

            # If the request was successful, the server will respond with a JSON object that includes an access token
            if response.status_code == 200:
                self.token = response.json().get("token")
                # print(f"Access token: {token}")
            else:
                print(
                    f"Failed to log in. Server responded with status code {response.status_code}."
                )
                self.token = None

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            self.token = None

    def get_user_profile(self):
        if self.token is None:
            return "No token available."

        url = "https://thinking-tester-contact-list.herokuapp.com/users/me"
        headers = {
            "Authorization": self.token,
        }

        try:
            response = requests.get(url, headers=headers)
            return response.json()

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def add_contact(self, contact_data):
        url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                url, headers=headers, data=json.dumps(contact_data)
            )
            return response.json()

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"


contact_data = {
    "firstName": "Willy",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "wd@fake.com",
    "phone": "8005555555",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "USA",
}

tester = ThinkingTester()
# print(tester.get_user_profile())
print(tester.add_contact(contact_data))
