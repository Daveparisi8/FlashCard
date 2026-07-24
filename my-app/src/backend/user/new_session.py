
import secrets
import string

existing_session_tokens = [] # <-- replace by DB


class NewSession:
    def __init__(self,):
        self.session_token = self.generate_token()

    def generate_token(self):
        while True:
            random_token = ''.join(
                secrets.choice(
                    string.ascii_uppercase + string.digits
                )
                for _ in range(25)
            )

            if random_token in existing_session_tokens:
                continue

            existing_session_tokens.append(random_token)
            return random_token
        