from django import forms
from .models import *

g = [['Male', 'Male'], ['Female', 'Female']]
c = [['python', 'Python'], ['SQL', 'SQL'], ['Django', 'Django']]
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    pno = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    add = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'cols':50, 'rows':10}))
    gender = forms.ChoiceField(choices=g, required=False, widget=forms.RadioSelect)
    cources = forms.MultipleChoiceField(choices=c, required=False, widget=forms.CheckboxSelectMultiple)
    username = forms.CharField( max_length=50, required=False)
    password = forms.CharField(max_length=50, required=False)
    

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'