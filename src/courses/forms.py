from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your Course Title"
        }
    ))

    class Meta:
        model = Course
        fields = [
            "title",
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title.")
        return title
