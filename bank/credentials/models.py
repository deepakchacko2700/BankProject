from django.db import models

# Create your models here.


class District(models.Model):
    district = models.CharField(max_length=200)

    def __str__(self):
        return self.district


class Branch(models.Model):
    branch = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch


class Account(models.Model):
    account_type = models.CharField(max_length=200)

    def  __str__(self):
        return self.account_type


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
    ]


class UserDetails(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True, blank=True)
    age = models.CharField('Age', max_length=3, null=True)
    gender = models.CharField('Gender',
                              max_length=1, choices= GENDER_CHOICES,
                              null=True)
    Phone_number = models.CharField('Phone number', max_length=10)
    mail_id = models.EmailField()
    address = models.TextField('Address')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    debit_card = models.BooleanField()
    credit_card = models.BooleanField()

    def __str__(self):
        return self.name























