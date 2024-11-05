from django.core.management.base import BaseCommand
from apps.university.models import *

class Command(BaseCommand):
    help = 'Update common_course for previously uploaded resources'

    def handle(self, *args, **kwargs):
        # Get all ResourcesQuestion entries
        questions = ResourcesQuestion.objects.all()
        books = ResourcesBook.objects.all()
        lectures = ResourcesLecture.objects.all()
        notes = ResourcesNote.objects.all()
        
        updated_count_question = 0
        for question in questions:
            # Check if the related course has common_courses
            if question.course and question.course.common_courses.exists():
                # Assign the common_courses to the question
                question.common_courses.set(question.course.common_courses.all())
                question.save()  # Save the updated object
                updated_count_question += 1
        
        updated_count_book = 0 
        for book in books:
            # Check if the related course has common_courses
            if book.course and book.course.common_courses.exists():
                # Assign the common_courses to the book
                book.common_courses.set(book.course.common_courses.all())
                book.save()  # Save the updated object
                updated_count_book += 1

        updated_count_lecture = 0
        for lecture in lectures:
            # Check if the related course has common_courses
            if lecture.course and lecture.course.common_courses.exists():
                # Assign the common_courses to the lecture
                lecture.common_courses.set(lecture.course.common_courses.all())
                lecture.save()  # Save the updated object
                updated_count_lecture += 1
                
        updated_count_note = 0
        for note in notes:
            # Check if the related course has common_courses
            if note.course and note.course.common_courses.exists():
                # Assign the common_courses to the note
                note.common_courses.set(note.course.common_courses.all())
                note.save()  # Save the updated object
                updated_count_note += 1

        self.stdout.write(self.style.SUCCESS(f"Updated {updated_count_question} questions, {updated_count_book} books, {updated_count_lecture} lectures, {updated_count_note} notes"))
