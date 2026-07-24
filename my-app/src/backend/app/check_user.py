"""
Authentication and account status validation.

This module:
- Validates a provided authentication token
- Checks the current account status
- Returns the authentication result
"""

def check_user_token(provided_token, auth_db_token):
    if provided_token == auth_db_token:
        return "active"
    
    return "rejected"

def check_user_status(auth_db_status):
    if auth_db_status == "active":
        return "active"

    return "rejected"

def check_user_password(provided_password, auth_db_password):
    if provided_password == auth_db_password:
        return "active"
    
    return "rejected"

def check_user_account(provided_token, auth_db_token, provided_password, auth_db_password, auth_db_status):
    token_status = check_user_token(provided_token, auth_db_token)
    password_status = check_user_password(provided_password, auth_db_password)
    account_status = check_user_status(auth_db_status)
    
    if token_status == "active" and password_status == "active" and account_status == "active":
        return "active"

    return "rejected"