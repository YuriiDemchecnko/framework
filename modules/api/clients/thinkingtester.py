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
            else:
                print(
                    f"Failed to log in. Server responded with status code {response.status_code}."
                )
                self.token = None

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            self.token = None

    def get_contact_list(self):
        url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
        headers = {
            "Authorization": self.token,
        }

        try:
            response = requests.get(url, headers=headers)
            # return response.json()  # Returns contact list
            return response.status_code

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def get_user_profile(self):
        if self.token is None:
            return "No token available."

        url = "https://thinking-tester-contact-list.herokuapp.com/users/me"
        headers = {
            "Authorization": self.token,
        }

        try:
            response = requests.get(url, headers=headers)
            # return response.json()
            return response.status_code

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
            return response.status_code  # returns 201 if OK

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def delete_contact(self, first_name):
        # Get the list of contacts
        contacts = self.get_contact_list()

        # Find the contact with the given first name and last name
        for contact in contacts:
            if contact["firstName"] == first_name:
                # If the contact is found, send a DELETE request to remove it
                url = f"https://thinking-tester-contact-list.herokuapp.com/contacts/{contact['_id']}"
                headers = {
                    "Authorization": self.token,
                }

                try:
                    response = requests.delete(url, headers=headers)
                    return response.status_code  # returns 200 if OK, None if not

                except requests.exceptions.RequestException as e:
                    return f"An error occurred: {e}"

    def update_contact(self, first_name, data):
        contacts = self.get_contact_list()
        for contact in contacts:
            if contact["firstName"] == first_name:
                # If the contact is found, send a PATCH request to update it
                url = f"https://thinking-tester-contact-list.herokuapp.com/contacts/{contact['_id']}"
                headers = {
                    "Authorization": self.token,
                }

                try:
                    response = requests.patch(url, headers=headers, json=data)
                    return response.status_code  # returns 200 if OK, None if not

                except requests.exceptions.RequestException as e:
                    return f"An error occurred: {e}"


# tester = ThinkingTester()
# print(tester.get_user_profile())
# print(tester.add_contact(contact_data))
# print(tester.get_contact_list())
# print(tester.delete_contact("Kelly"))
# print(tester.update_contact("Dolly", data_to_update))
