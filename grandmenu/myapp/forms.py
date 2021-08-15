from django import forms
from django.forms.models import ModelChoiceField
from .models import StoreInfo, StoreMenu

"""========================================================
店舗情報作成・編集用フォーム
model:  StoreInfo
========================================================"""
class StoreInfoForm(forms.ModelForm):
    class Meta:
        model = StoreInfo
        fields = ('STORE_EMAIL', 'STORE_NAME', 'STORE_POSTAL_CODE', 'STORE_ADDRESS', 'STORE_TEL')
        # fields = '__all__'    #すべて取得する　本来こちらを使用 ↑上記のようにpickもできる
        labels = {
            'STORE_EMAIL': 'E_Mail',
            'STORE_NAME': '店名',
            'STORE_POSTAL_CODE': '郵便番号',
            'STORE_ADDRESS': '住所',
            'STORE_TEL': '電話番号'
        }
        help_texts = {
            'STORE_EMAIL': 'E_Mailを入力',
            'STORE_NAME': '店名を入力',
            'STORE_POSTAL_CODE': '郵便番号を入力',
            'STORE_TEL': '電話番号を入力'
        }

        widgets = {
            'STORE_NAME': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': 'E_Mail'}),
            'STORE_POSTAL_CODE': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': '郵便番号'}),
            'STORE_ADDRESS': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': '住所'}),
            'STORE_TEL': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': '電話番号'})
        }



        exclude = ["STORE_EMAIL"]       #Form入力の除外を行う


class StoreMenuForm(forms.ModelForm):
    STORE_INFO = ModelChoiceField(queryset=StoreInfo.objects.all(), required=False)

    class Meta:
        model = StoreMenu
        fields = '__all__'

        widgets = {
            'CLASS1': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': 'CLASS1'}),
            'CLASS2': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': 'CLASS2'}),
            'CLASS3': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': 'CLASS3'}),
            'PLICE': forms.TextInput(attrs={'class': 'text_box--small', 'placeholder': 'PLICE'})
        }

        exclude = ["STORE_INFO", "CLASS1_ID", "CLASS2_ID", "CLASS3_ID"]       #Form入力の除外を行う
