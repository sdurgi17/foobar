from django import forms

class NameForm(forms.Form):
    Header = forms.CharField(label='header', max_length=100)
    Project = forms.CharField(label='project', max_length=100)
    Body = forms.CharField(label = 'body', widget=forms.Textarea)
