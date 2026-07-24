
from check_user import check_user_account
from new_user import NewUserRegistration
from BLL import login_request
from new_session import NewSession

new_user = NewUserRegistration("example_user", "example_password")
new_session = NewSession()

# Display the details of the newly registered user
print(f"user name: {new_user.account_name}, user password: {new_user.account_password}, user token: {new_session.session_token}")

# Validate check_user
check_result = check_user_account(new_session.session_token, new_session.session_token, new_user.account_password, new_user.account_password, "active")
print(f"Check user account result: {check_result}")

def test_login_reqeust():
    """Simple interactive CLI to validate login behavior end-to-end."""

    print("\n=== Login Request CLI Test ===")
    print("This test executes: check_user_account(...) -> login_request(...)")

    while True:
        print("\nChoose a test option:")
        print("1) Happy path (valid token + password + active status)")
        print("2) Invalid token")
        print("3) Invalid password")
        print("4) Inactive account status")
        print("5) Custom input test")
        print("6) Register a fresh test user then test")
        print("0) Exit")

        choice = input("Selection: ").strip()

        if choice == "0":
            print("Exiting login CLI test.")
            break

        if choice == "1":
            provided_token = new_session.session_token
            auth_db_token = new_session.session_token
            provided_password = new_user.account_password
            auth_db_password = new_user.account_password
            auth_db_status = "active"
        elif choice == "2":
            provided_token = "WRONGTOKEN123"
            auth_db_token = new_session.session_token
            provided_password = new_user.account_password
            auth_db_password = new_user.account_password
            auth_db_status = "active"
        elif choice == "3":
            provided_token = new_session.session_token
            auth_db_token = new_session.session_token
            provided_password = "wrong_password"
            auth_db_password = new_user.account_password
            auth_db_status = "active"
        elif choice == "4":
            provided_token = new_session.session_token
            auth_db_token = new_session.session_token
            provided_password = new_user.account_password
            auth_db_password = new_user.account_password
            auth_db_status = "rejected"
        elif choice == "5":
            provided_token = input("Provided token: ").strip()
            auth_db_token = input("Auth DB token: ").strip()
            provided_password = input("Provided password: ").strip()
            auth_db_password = input("Auth DB password: ").strip()
            auth_db_status = input("Auth DB status (active/rejected): ").strip().lower()
        elif choice == "6":
            account_name = input("New account name: ").strip()
            account_password = input("New account password: ").strip()

            test_user = NewUserRegistration(account_name, account_password)
            test_session = NewSession()
            print(
                f"Generated user -> name: {test_user.account_name}, "
                f"password: {test_user.account_password}, token: {test_session.session_token}"
            )

            provided_token = input("Provided token (press Enter to use generated token): ").strip() or test_session.session_token
            auth_db_token = test_session.session_token
            provided_password = input("Provided password (press Enter to use generated password): ").strip() or test_user.account_password
            auth_db_password = test_user.account_password
            auth_db_status = input("Auth DB status (default active): ").strip().lower() or "active"
        else:
            print("Invalid option. Please choose 0-6.")
            continue

        account_check_result = check_user_account(
            provided_token,
            auth_db_token,
            provided_password,
            auth_db_password,
            auth_db_status,
        )

        login_result = login_request(account_check_result)

        print("\n--- Test Result ---")
        print(f"check_user_account result: {account_check_result}")
        print(f"login_request result: {login_result}")


def test_login_request():
    return test_login_reqeust()


if __name__ == "__main__":
    test_login_reqeust()
        