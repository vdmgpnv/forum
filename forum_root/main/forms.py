from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    post_text = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Post
        fields = ('post_text',)    
    
class CreateThread(forms.Form):
    thread_name = forms.CharField(max_length=100, help_text='Название темы')
    post_text = forms.CharField(label='Description',
                   widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    
    class Meta:
        fields = ('thread_name', 'post_text')