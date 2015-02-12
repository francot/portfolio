from django import forms
from portfolio.models import Job, JobCategory


class PostForm(forms.ModelForm):
    model = Post
    fields = ['title', 'description', 'category', 'secondary_category', 'job_date', 'image', 'priority']
    
