from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.utils.safestring import mark_safe

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, mark_safe(
                f"প্রিয় <strong>{feedback.user.profile.fullname}</strong>!, আপনার মূল্যবান মন্তব্যের জন্য অসংখ্য ধন্যবাদ! Onebyzero Edu থেকে আপনি যাতে আরও উপকৃত হতে পারেন সেই লক্ষ্য ও প্রত্যাশা নিয়েই আমরা প্রতিনিয়ত বিভিন্ন চেষ্টা করে যাচ্ছি।"
                ))
            return redirect('display_feedbacks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def display_feedbacks(request):
    # feedbacks = Feedback.objects.filter(is_approved=True).order_by('-created_at')
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/display_feedbacks.html', {'feedbacks': feedbacks})
