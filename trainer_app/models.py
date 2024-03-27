from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Trainer(AbstractUser):
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length = 255,
        unique = True
    )
    #django auto creates a username field, indicate here username field is actually email
    USERNAME_FIELD = 'email'
    #username and password already required. This is in case we have more required. Nonetheless still required to write.
    REQUIRED_FIELDS = []
