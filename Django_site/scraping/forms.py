from django.forms import ModelForm
from .models import Post

class LinkForm(ModelForm):
    class Meta:
        model = Post
        fields = ['URL']
