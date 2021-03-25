
from .models import *
from django import forms


class PostCreationForm(forms.ModelForm):



    class Meta:
        model = Post
        widgets = {
            'title':forms.TextInput(attrs={'class':'single-input','placeholder':'Yazı Başlığı'}),
            'content':forms.Textarea(attrs={'class':'single-input','placeholder':'İçerik'}),
        }


        fields = [
            'title',
            'category',
            'content',
            'image',

        ]