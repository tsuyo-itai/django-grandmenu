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
            'STORE_ADDRESS': '住所を入力',
            'STORE_TEL': '電話番号を入力'
        }

        exclude = ["STORE_EMAIL"]       #Form入力の除外を行う


class StoreMenuForm(forms.ModelForm):
    STORE_INFO = ModelChoiceField(queryset=StoreInfo.objects.all(), required=False)

    class Meta:
        model = StoreMenu
        fields = '__all__'

        exclude = ["STORE_INFO", "CLASS1_ID", "CLASS2_ID", "CLASS3_ID"]       #Form入力の除外を行う
