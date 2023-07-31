from django.db import models

# Create your models here.
# ExcelCalculate > main > models.py

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True)  # 이메일 필드는 EmailField로 사용하는 것이 좋습니다.
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)  # 불리언 필드로 사용해야 합니다.
