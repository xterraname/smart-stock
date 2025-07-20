from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator


phone_number_validator = RegexValidator(
    r"^\+998[\d]{9}", 
    message="The phone number must be in the format +998901234567"
)

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password=None):
        if not phone_number:
            raise ValueError("Users must have an phone number")
        
        if not full_name:
            raise ValueError("User must have an full name")

        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password=None):
        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[phone_number_validator],
        verbose_name="Phone number"
    )
    full_name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]
    
    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

