from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view_book", "Can view book"),
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None ):
        if not email:
            raise ValueError("User Must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email,password=None):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)
        return self.create_user(username, email, password)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', null= True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    def __str__ (self):
        return self.username