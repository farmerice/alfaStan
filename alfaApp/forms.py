from django import forms

from .models import Defect

class PostForm(forms.ModelForm):

    class Meta:
        model = Defect
        fields = ('title','project','apartment','description')
