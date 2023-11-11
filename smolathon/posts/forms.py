from django import forms


class PostSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={'class': 'search__input none', 'placeholder': 'поиск'})
    )