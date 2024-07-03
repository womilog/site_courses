from django import forms

from courses.models import Course, Comment


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'desc', 'image']
        widgets = {'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})}
        labels = {'slug': 'Название URL'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
