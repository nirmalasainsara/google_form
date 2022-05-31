from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField
# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class User(models.Model):
    """
    A User Model.
    """
    # name = models.CharField(
    #     _('Name'),
    #     max_length=30,
    # )

    # gender = models.CharField(
    #     _('Gender'),
    #     max_length=10,
    #     choices = GENDER_CHOICES
    # )

    # age = models.PositiveIntegerField(
    #     _('Age'),
    #     null=True,
    #     blank=True,
    # )

    # dob = models.DateField(
    #      _('Date Of Birth'),
    #     null=True,
    #     blank=True,
    # )

    data = JSONField(_("Data"), blank=True, null=True)


class Customer(models.Model):
    """
    A Custom User Model.
    """
    name = models.CharField(
        _('Name'),
        max_length=20,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        _('Email'),
        unique=True,
        null=True,
        blank=True,
    )
    user_form = JSONField(_("User Form"), blank=True, null=True)

    # google_form = models.ForeignKey(
    #     User,
    #     _('google form'),
    #     on_delete=models.CASCADE,
    #     related_name='Google Form',
    # )