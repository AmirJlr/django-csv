from django import forms

class CsvForm(forms.Form):
    csv_upload = forms.FileField()

    