from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Event
from django.utils import timezone

# Quiz Submission Form
class QuizSubmissionForm(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            "class": "border px-3 py-2 rounded w-full"
        })
    )

# Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
# Quiz Creation Form
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "border px-3 py-2 rounded w-full"
            }),
            "description": forms.Textarea(attrs={
                "class": "border px-3 py-2 rounded w-full",
                "rows": 4
            })
        }
        
# Event Creation Form
class EventForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Event Title",
        widget=forms.TextInput(attrs={
            "class": "border px-3 py-2 rounded w-full"
        })
    )
    date = forms.DateField(
        label="Event Date",
        widget=forms.DateInput(attrs={
            "class": "border px-3 py-2 rounded w-full",
            "type": "date",
            "min": timezone.now().date().isoformat()  # Prevent past dates
        })
    )
    location = forms.CharField(
        max_length=200,
        required=False,
        label="Location",
        widget=forms.TextInput(attrs={
            "class": "border px-3 py-2 rounded w-full"
        })
    )
    description = forms.CharField(
        required=False,
        label="Description",
        widget=forms.Textarea(attrs={
            "class": "border px-3 py-2 rounded w-full",
            "rows": 4
        })
    )