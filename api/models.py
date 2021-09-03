from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

User = get_user_model()


class Organisation(models.Model):
    title = models.CharField('Title', max_length=30, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField('Address', max_length=100, blank=True)
    description = models.TextField('Description', max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=10)
    last_name = models.CharField('Last name', max_length=20)
    middle_name = models.CharField('Middle name', max_length=20, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField('Position', max_length=20)
    phone_regex = RegexValidator(
        regex=r'^\+\d{9,15}$',
        message="Phone number must be entered in the format: '+70123456789'."
                "from 9 up to 15 digits allowed.")
    private_phone = models.CharField('Private phone', validators=[phone_regex], max_length=15,
                                     unique=True, blank=True)
    work_phone = models.CharField('Work phone', validators=[phone_regex], max_length=15, blank=True)
    fax = models.CharField('Fax', validators=[phone_regex], max_length=15, blank=True)
    organisation = models.ForeignKey(
        'Organisation',
        on_delete=models.CASCADE,
        blank=True,
        related_name='employees'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'organisation'],
                name='unique_organisations_employee'
            )
        ]
