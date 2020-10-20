from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }
    ))
    # this is how you override the attributes of the field with the same name underneath
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # field validation
    # function name in this format: clean_<field_name>
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "karina" not in title:
            raise forms.ValidationError("This is not a valid title!")
        return title



class RawProductForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Your Title"}
    ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-2",
                "rows": 20,
                "cols": 120
            }
        )
    )