from django import forms
from blogu.models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the blog")
    views = forms.IntegerField(widget=forms.HiddenInput,initial=0)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)
    image=forms.ImageField(required=False)
    image_description=forms.CharField(widget=forms.Textarea,required=False)
    text = forms.CharField(widget=forms.Textarea,help_text="Enter the blog here")
    likes=forms.IntegerField(widget=forms.HiddenInput,initial=0)
    
    class Meta:
    	model=Blog
    	fields = ('title','image','image_description','text',)
    
