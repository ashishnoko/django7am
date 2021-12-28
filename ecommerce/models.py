from django.db import models


# Create your models here.
class Setting(models.Model):
    c_name = models.CharField(max_length=255, unique=True)
    c_email = models.CharField(max_length=255, unique=True)
    c_email_1 = models.CharField(max_length=255, unique=True, null=True, blank=True)
    c_email_2 = models.CharField(max_length=255, unique=True, null=True, blank=True)
    c_phone = models.CharField(max_length=30)
    c_phone1 = models.CharField(max_length=30, null=True, blank=True)
    c_phone2 = models.CharField(max_length=30, null=True, blank=True)
    c_address = models.CharField(max_length=30)
    c_logo = models.ImageField(upload_to='logo', null=True, blank=True)
    c_meta_title = models.TextField()
    c_meta_description = models.TextField()

    def __str__(self):
        return self.c_name

    def get_company_name(self):
        c_name = str(self.c_name)
        return c_name.title()
