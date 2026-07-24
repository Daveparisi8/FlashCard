"""
Authentication and account status validation.

This module:
- Validates a provided authentication token
- Checks the current account status
- Returns the authentication result
"""


####  Helper Functions

def check_user_token(provided_token, auth_db_token):
    """Validate the provided authentication token against the token stored in the authentication database.
    
    Args:
        provided_token (str): The token provided by the user.
        auth_db_token (str): The token stored in the authentication database.

    Returns:
        str: "active" if the tokens match, "rejected" otherwise.
    """
    if provided_token == auth_db_token:
        return "active" 
    return "rejected"

def check_user_status(auth_db_status):
    """
    Validate the current account status.
    
    Args:
        auth_db_status (str): The current status of the account in the authentication database.

    Returns:
        str: "active" if the account status is active, "rejected" otherwise.
    """
    if auth_db_status == "active":
        return "active"
    return "rejected"

def check_user_password(provided_password, auth_db_password):
    """
    Validate the provided password against the password stored in the authentication database.
    
    Args:
        provided_password (str): The password provided by the user.
        auth_db_password (str): The password stored in the authentication database.

    Returns:
        str: "active" if the passwords match, "rejected" otherwise.
    """
    if provided_password == auth_db_password:
        return "active"
    return "rejected"

def check_user_account(provided_token, auth_db_token, provided_password, auth_db_password, auth_db_status):
    """
    Validate the user account by checking the authentication token, password, and account status.
    
    Args:
        provided_token (str): The token provided by the user.
        auth_db_token (str): The token stored in the authentication database.
        provided_password (str): The password provided by the user.
        auth_db_password (str): The password stored in the authentication database.
        auth_db_status (str): The current status of the account in the authentication database.

    Returns:
        str: "active" if the token, password, and account status are all active, "rejected" otherwise.
    """
    token_status = check_user_token(provided_token, auth_db_token)
    password_status = check_user_password(provided_password, auth_db_password)
    account_status = check_user_status(auth_db_status)
    
    if token_status == "active" and password_status == "active" and account_status == "active":
        return "active"
    return "rejected"