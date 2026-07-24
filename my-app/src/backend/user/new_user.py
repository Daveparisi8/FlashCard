
class NewUserRegistration:

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    def register_user(self):

        return {
            "user_info": {
                "account_name": self.account_name,
                "account_password": self.account_password
            }
        }
