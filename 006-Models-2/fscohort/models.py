from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField('Numara')
    about = models.TextField('Hakkında', blank=True, null=True )
    avatar = models.ImageField('Resim', upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.number} - {self.first_name} {self.last_name} '

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Öğrenciler'