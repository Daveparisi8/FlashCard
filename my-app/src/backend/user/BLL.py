#  This component will:
#  match token to user account; and validate account status as active or rejected


## Token Match


def login_request(check_user_account):

    if check_user_account == "active":
        return True
    return "Incorrect Credentials. Please try again."
