from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class StoreInfo(models.Model):
    STORE_EMAIL =           models.EmailField(max_length=254, unique=True)
    STORE_NAME =            models.CharField(max_length=70)
    postal_code_regex =     RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    STORE_POSTAL_CODE =     models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    STORE_ADDRESS =         models.CharField(max_length=100)
    tel_number_regex =      RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    STORE_TEL =             models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')

    def __str__(self):
        return self.STORE_NAME