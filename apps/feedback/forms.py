from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'cols': 80,
                'class': 'form-control',  # Bootstrap class for consistent styling
                'placeholder': 'Onebyzero Edu ব্যবহার করে আপনি যদি বিন্দুমাত্র উপকৃত হয়ে থাকেন তাহলে সেই অনুভূতিটা আমাদের সাথে প্রকাশ করতে পারেন।',
                'style': 'resize: none; border-radius: 8px;',  # Disabling resize and adding custom border-radius
            }),
        }
