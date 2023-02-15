from django.db import models

class Registration(models.Model):
    name = models.CharField('Название отеля', max_length=100)
    city = models.CharField('Город', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

class Booking(models.Model):
    hotel = models.CharField('Название отеля', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Отчество', max_length=50)
    number = models.CharField('Номер телефона', max_length=15)
    #tg = models.BooleanField('tg', default=False)
