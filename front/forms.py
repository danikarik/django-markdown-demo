from django import forms
from markdownx.fields import MarkdownxFormField

class MDForm(forms.Form):
    mdfield = MarkdownxFormField()
