"""
Documentation and license information goes here.
"""

from django.views.generic import FormView
from .forms import IndexForm

class IndexView(FormView):
    """An example of a simple class based generic view"""
    template_name = "index.html"
    form_class = IndexForm
    success_url="/"
        
