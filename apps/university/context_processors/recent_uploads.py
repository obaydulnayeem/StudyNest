from apps.university.models import *
from django.utils import timezone

def format_upload_time(upload_time):
    current_time = timezone.now()
    duration = current_time - upload_time
    seconds_ago = duration.total_seconds()

    def pluralize(value, unit):
        return f"{value} {unit}" + ("s" if value != 1 else "")

    if seconds_ago < 60:
        return pluralize(int(seconds_ago), "second") + " ago"
    elif seconds_ago < 3600:
        return pluralize(int(seconds_ago / 60), "minute") + " ago"
    elif seconds_ago < 86400:
        return pluralize(int(seconds_ago / 3600), "hour") + " ago"
    elif seconds_ago < 604800:
        return pluralize(int(seconds_ago / 86400), "day") + " ago"
    elif seconds_ago < 2419200:
        return pluralize(int(seconds_ago / 604800), "week") + " ago"
    elif seconds_ago < 29030400:
        return pluralize(int(seconds_ago / 2419200), "month") + " ago"
    else:
        return pluralize(int(seconds_ago / 29030400), "year") + " ago"

def recent_uploads_view(request):
    context = {}

    # Handle latest question
    latest_question = ResourcesQuestion.objects.last()
    if latest_question:
        context['uploader_latest_question'] = latest_question.uploaded_by.fullname
        context['latest_question'] = latest_question
        context['formatted_time_latest_question'] = format_upload_time(latest_question.upload_time)
        context['question_uploader_for_profile_info'] = latest_question.uploaded_by
    else:
        context['uploader_latest_question'] = None
        context['latest_question'] = None
        context['formatted_time_latest_question'] = None
        context['question_uploader_for_profile_info'] = None

    # Handle latest book
    latest_book = ResourcesBook.objects.last()
    if latest_book:
        context['uploader_latest_book'] = latest_book.uploaded_by.fullname
        context['latest_book'] = latest_book
        context['formatted_time_latest_book'] = format_upload_time(latest_book.upload_time)
        context['book_uploader_for_profile_info'] = latest_book.uploaded_by
    else:
        context['uploader_latest_book'] = None
        context['latest_book'] = None
        context['formatted_time_latest_book'] = None
        context['book_uploader_for_profile_info'] = None

    # Handle latest note
    latest_note = ResourcesNote.objects.last()
    if latest_note:
        context['uploader_latest_note'] = latest_note.uploaded_by.fullname
        context['latest_note'] = latest_note
        context['formatted_time_latest_note'] = format_upload_time(latest_note.upload_time)
        context['note_uploader_for_profile_info'] = latest_note.uploaded_by
    else:
        context['uploader_latest_note'] = None
        context['latest_note'] = None
        context['formatted_time_latest_note'] = None
        context['note_uploader_for_profile_info'] = None

    # Handle latest lecture
    latest_lecture = ResourcesLecture.objects.last()
    if latest_lecture:
        context['uploader_latest_lecture'] = latest_lecture.uploaded_by.fullname
        context['latest_lecture'] = latest_lecture
        context['formatted_time_latest_lecture'] = format_upload_time(latest_lecture.upload_time)
        context['lecture_uploader_for_profile_info'] = latest_lecture.uploaded_by
    else:
        context['uploader_latest_lecture'] = None
        context['latest_lecture'] = None
        context['formatted_time_latest_lecture'] = None
        context['lecture_uploader_for_profile_info'] = None

    return context
