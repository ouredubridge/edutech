from django import forms
from .models import Course, Module, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'instructor', 'price']

        """widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder: 'Course Title'})
        }"""

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Module Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Module Description'}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lesson Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Lesson Content', 'id': 'tinymce-content'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lesson Order'}),
        }