def get_coupon(day):
    coupons = {
        'Monday': 'MON10',
        'Tuesday': 'TUE15',
        'Wednesday': 'WED20',
        'Thursday': 'THU25',
        'Friday': 'FRI30',
        'Saturday': 'SAT35',
        'Sunday': 'SUN40'
    }
    return coupons.get(day, 'Invalid day')

# Example usage
day = 'Wednesday'
print(get_coupon(day))
