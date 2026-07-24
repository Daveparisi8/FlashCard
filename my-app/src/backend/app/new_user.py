# This component will handle new user registration
# It will:
# - collect user information
# - assign a randomized token for future use

import secrets
import string

class NewUserRegistration:

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password
        self.token = self.generate_token()

    def generate_token(self):
        random_token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(25))
        random_token = random_token.upper()
        return random_token
    
    def register_user(self):

        return {
            "user_info": {
                "account_name": self.account_name,
                "account_password": self.account_password
            },
            "token": self.token
        }

# Example usage of the NewUserRegistration class. This will feed into Auth DB.
new_user = NewUserRegistration("example_user", "example_password")
print(f"user name: {new_user.account_name}, user password: {new_user.account_password}, user token: {new_user.token}")
