from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def humanize_duration(duration):
    if isinstance(duration, str):
        try:
            # Convert the string to a datetime object
            approved_at = datetime.strptime(duration, "%b. %d, %Y, %I:%M %p")
            # Calculate the difference
            duration = datetime.now() - approved_at
        except ValueError as e:
            # Log error for debugging purposes
            print(f"Error parsing date string '{duration}': {e}")
            return ""
    
    if isinstance(duration, timedelta):
        total_seconds = int(duration.total_seconds())
        years, remainder = divmod(total_seconds, 31536000)  # 365 days * 24 * 60 * 60
        months, remainder = divmod(remainder, 2592000)      # 30 days * 24 * 60 * 60
        days, remainder = divmod(remainder, 86400)          # 24 * 60 * 60

        if years > 0:
            return f"{years} years, {months} months, {days} days"
        elif months > 0:
            return f"{months} months, {days} days"
        elif days > 0:
            return f"{days} days"
        else:
            return "Less than a day"
    else:
        # Return an empty string for invalid types
        return ""
