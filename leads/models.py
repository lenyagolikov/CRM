from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    """
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        "Agent", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('leads:lead-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('leads:lead-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('leads:lead-delete', kwargs={'pk': self.pk})


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('agents:agent-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('agents:agent-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('agents:agent-delete', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return self.user.username


def post_user_created_signal(sender, instance, created, **kwargs):
    """Created UserProfile for new user"""
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
