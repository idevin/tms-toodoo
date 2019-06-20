from django import forms


class ListForm(forms.Form):
    title = forms.CharField(label=False, max_length=255, required=True)
