from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] ='text_box--small'
        self.fields['username'].widget.attrs['placeholder'] ='登録メールアドレス'
        self.fields['password'].widget.attrs['class'] ='text_box--small'
        self.fields['password'].widget.attrs['placeholder'] ='パスワード'

        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] ='text_box--small'
        self.fields['email'].widget.attrs['placeholder'] ='登録メールアドレス'
        self.fields['password1'].widget.attrs['class'] ='text_box--small'
        self.fields['password1'].widget.attrs['placeholder'] ='パスワード'
        self.fields['password2'].widget.attrs['class'] ='text_box--small'
        self.fields['password2'].widget.attrs['placeholder'] ='パスワード(確認用)'

        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email