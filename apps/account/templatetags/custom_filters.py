# account/templatetags/custom_filters.py
from django import template
from collections import defaultdict

register = template.Library()

@register.filter
def groupby(courses, attribute):
    grouped_courses = defaultdict(list)
    for course in courses:
        key = getattr(course, attribute)
        grouped_courses[key].append(course)
    return grouped_courses.items()
