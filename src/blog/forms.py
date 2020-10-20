from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your Article Title"
        }
    ))

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "active"
        ]
