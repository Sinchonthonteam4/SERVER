from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager as DjangoUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class University(models.Model):
    univ_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

## 함수 재정의
class UserManager(DjangoUserManager):
    def _create_user(self, email,password, **extra_fields):
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email, password,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        user = self._create_user(email,password,**extra_fields)
        return user
    
    def create_superuser(self, email, password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        user = self._create_user(email,password,**extra_fields).save()
        return user
    
# 메인 유저 모델
class User(AbstractUser):
    username = None
    email = models.EmailField("이메일 주소", unique=True)
    USERNAME_FIELD = 'email'

    nick_name = models.CharField("닉네임", max_length=10,default="익명")
    university = models.ForeignKey('University',on_delete=models.CASCADE,default=None,null=True)
    
    REQUIRED_FIELDS = []
    objects = UserManager()
