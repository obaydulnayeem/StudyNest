# templatetags/custom_filters.py
from django import template

register = template.Library()

def semester_converter(semester):
    if semester == 1:
        return '1st'
    elif semester == 2:
        return '2nd'
    elif semester == 3:
        return '3rd'
    elif semester == 4:
        return '4th'
    elif semester == 5:
        return '5th'
    elif semester == 6:
        return '6th'
    elif semester == 7:
        return '7th'
    elif semester == 8:
        return '8th'
    elif semester == '1st':
        return 1
    elif semester == '2nd':
        return 2
    elif semester == '3rd':
        return 3
    elif semester == '4th':
        return 4
    elif semester == '5th':
        return 5
    elif semester == '6th':
        return 6
    elif semester == '7th':
        return 7
    elif semester == '8th':
        return 8
    else:
        return None

register.filter('semester_converter', semester_converter)
