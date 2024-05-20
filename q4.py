import re

def validate_phone_number(phone):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(phone) is not None

# Example usage
phone = "+1234567890"
print(validate_phone_number(phone))  # True or False
