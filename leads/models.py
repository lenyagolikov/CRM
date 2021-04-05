from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    """
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return self.user.username
