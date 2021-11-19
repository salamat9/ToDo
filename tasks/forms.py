from django import forms
from .models import Category, Task, Tag


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category name')

    class Meta:
        model = Category
        fields = ['name']


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    tags = forms.CharField()

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'tags', 'category']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags').split()
        for tag in tags:
            if tag[0] != '#':
                raise forms.ValidationError('Invalid tag!')
        return tags


# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['name']
