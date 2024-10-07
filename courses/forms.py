from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'instructor', 'price']

        """widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder: 'Course Title'})
        }"""