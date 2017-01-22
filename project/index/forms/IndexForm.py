"""
Produces html for submission of a form.
"""

from django import forms as f

class IndexForm(f.Form):
    github_url = f.CharField(max_length=255, min_length=2)
