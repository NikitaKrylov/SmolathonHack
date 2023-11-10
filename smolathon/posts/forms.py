from django import forms


class PostSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )