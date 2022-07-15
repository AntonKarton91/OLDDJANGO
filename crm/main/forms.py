# from django.contrib.auth import password_validation
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django import forms
#
# from .models import *
#
# class RegisterUserForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="Пароль",
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password" , 'class': 'form-input'}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#
#     password2 = forms.CharField(
#         label="Подтверждение пароля",
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password" , 'class': 'form-input'}),
#         strip=False,
#         help_text="Enter the same password as before, for verification.",
#     )
#
#     img = forms.FileField(required=False,
#                           label="Фото",)
#
#     class Meta:
#         model=CustomUser
#         fields=('first_name',
#                 'sur_name',
#                 'email',
#                 'password1',
#                 'password2',
#                 'department',
#                 'stage',
#                 'img',
#                 )
#
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'sur_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'email': forms.TextInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
#             'department': forms.Select(attrs={'class': 'form-input'}),
#             'stage': forms.Select(attrs={'class': 'form-input'}),
#
#         }
#
# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-input'}))
#     password = forms.CharField(
#         label="Пароль",
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-input'}),
#     )
#     class Meta:
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
#             }
#
#
# class CreateTaskForm(forms.ModelForm):
#     task_describe=forms.TextInput
#     # points=forms.IntegerField(min_value=0)
#     class Meta:
#         model=Tasks
#         fields = ['task_number',
#                   'task_title',
#                   'points',
#                   'participants1',
#                   'task_describe',]
#
#         widgets = {
#             'task_number': forms.TextInput(attrs={'class': 'form-input1'}),
#             'task_title': forms.TextInput(attrs={'class': 'form-input1'}),
#             'points': forms.TextInput(attrs={'class': 'form-input1'}),
#             'task_describe': forms.Textarea(attrs={'class': 'form-input1'}),
#             'participants1': forms.CheckboxSelectMultiple(attrs={'class': 'form-input1'}),
#         }
#
#
# class CreateComment(forms.ModelForm):
#     comment = forms.TextInput()
#     class Meta:
#         model=TaskComments
#         fields = ['comment',
#                   ]
#
#         widgets = {
#             'comment': forms.TextInput(attrs={'class': 'form_input_com', 'placeholder':' Введите комментарий'}),
#         }
#
#
#
# class CreateClient(forms.ModelForm):
#
#     class Meta:
#         model=Client
#         fields = ['client_name',
#                   ]
#
#         widgets = {
#             'client_name': forms.TextInput(attrs={'class': 'form_input1', 'placeholder':' Введите название'}),
#         }
#
# class CreateEquipmentCat(forms.ModelForm):
#
#     class Meta:
#         model=EquipmentCat
#         fields = ['cat_name',
#                   ]
#
#         widgets = {
#             'cat_name': forms.TextInput(attrs={'class': 'form_input1', 'placeholder':' Введите название'}),
#         }
#
# # class CreateEquipment(forms.ModelForm):
