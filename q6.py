class UserError(Exception):
    pass

class NotUniqueError(UserError):
    pass

class NotPositiveIntegerError(UserError):
    pass

class UnderAgeError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

def validate_user_data(users):
    usernames = set()
    for user in users:
        username, email, age = user
        if username in usernames:
            raise NotUniqueError(f"Username {username} is not unique")
        if not isinstance(age, int) or age <= 0:
            raise NotPositiveIntegerError(f"Age {age} is not a positive integer")
        if age < 16:
            raise UnderAgeError(f"User {username} is under 16")
        if not re.match(r'^\w+@\w+\.\w+$', email):
            raise InvalidEmailError(f"Email {email} is invalid")
        usernames.add(username)

# Example usage
users = [
    ('alice', 'alice@example.com', 20),
    ('bob', 'bob@example.com', 15),
    ('charlie', 'charlie@example.com', 17)
]

try:
    validate_user_data(users)
except UserError as e:
    print(e)
