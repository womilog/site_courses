from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Введите Email', required=True, help_text='Нельзя вводить символы: @, /, _',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}))
    username = forms.CharField(label='Введите Логин', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label='Введите пароль', required=True, help_text='Пароль не должен быть простым',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Введите Email', required=True, help_text='Нельзя вводить символы: @, /, _',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}))
    username = forms.CharField(label='Введите Логин', required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    male = forms.ChoiceField(choices=CHOICES)
    accept = forms.BooleanField(label='Согласие на отправку уведомлений на почту ')


    class Meta:
        model = User
        fields = ['email', 'username', 'male', 'accept']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузит фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
