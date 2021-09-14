from django.db import models
import datetime 

# Create your models here.

class Accrual(models.Model):
    MONTH_CHOICE = [(m,m) for m in range(1,13)]
    
    date = models.DateField()
    month = models.IntegerField(choices=MONTH_CHOICE)
    
    def __str__(self):
        return "Долг {}".format(self.pk)
    
    class Meta:
        verbose_name = "Долг"
        verbose_name_plural = "Долги"
        ordering = ['date']


    # date = models.DateField(_("Date"), default=datetime.date.today)

class Payment(models.Model):
    MONTH_CHOICE = [(m,m) for m in range(1,13)]
    
    date = models.DateField()
    month = models.IntegerField(choices=MONTH_CHOICE)
    
    def __str__(self):
        return "Платеж {}".format(self.pk)
    
    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ['date']
