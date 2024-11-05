from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now
import datetime

register = template.Library()

@register.filter(name='time_ago')
def time_ago(value):
    if isinstance(value, datetime.datetime):
        delta = now() - value
        seconds = delta.total_seconds()

        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            return f"{int(seconds/60)}m"
        elif seconds < 86400:
            return f"{int(seconds/3600)}h"
        elif seconds < 604800:
            return f"{int(seconds/86400)}d"
        elif seconds < 2628000:
            return f"{int(seconds/604800)}w"
        elif seconds < 31536000:
            return f"{int(seconds/2628000)}mo"
        else:
            return f"{int(seconds/31536000)}y"
    
    return value  # Return the original value if it's not a datetime object
