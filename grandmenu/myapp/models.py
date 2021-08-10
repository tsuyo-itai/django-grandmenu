from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class StoreInfo(models.Model):
    STORE_EMAIL =           models.EmailField(max_length=254, unique=True, null=True)
    STORE_NAME =            models.CharField(max_length=70)
    postal_code_regex =     RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    STORE_POSTAL_CODE =     models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    STORE_ADDRESS =         models.CharField(max_length=100)
    tel_number_regex =      RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    STORE_TEL =             models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')

    def __str__(self):
        return self.STORE_NAME


class StoreMenu(models.Model):
    #menuIDはデフォルトで設定されているid
    STORE_INFO = models.ForeignKey(StoreInfo, on_delete=models.CASCADE, null=True, blank=True)
    CLASS1_ID = models.IntegerField(default=1)
    CLASS1 = models.CharField(max_length=50)
    CLASS2_ID = models.IntegerField(default=1)
    CLASS2 = models.CharField(max_length=50)
    CLASS3_ID = models.IntegerField(default=1)
    CLASS3 = models.CharField(max_length=50)
    PLICE = models.IntegerField()

    def __str__(self):
        return self.CLASS3
