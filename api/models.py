from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Organisation(models.Model):
    title = models.CharField('Title', max_length=30, unique=True)
    address = models.TextField('Address', max_length=30, blank=True)
    description = models.TextField('Description', max_length=30, blank=True)
    employee = models.ManyToManyField(
        'Employee',
        max_length=30
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Employee(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    middle_name = models.CharField('Middle name', max_length=30, blank=True)
    position = models.CharField('Position', max_length=30)
    private_phone = PhoneNumberField('Private', unique=True)
    work_phone = PhoneNumberField('Work_phone')
    fax = PhoneNumberField('Fax', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmployeeOrganisation(models.Model):
    organisation = models.ForeignKey('Organisation', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
