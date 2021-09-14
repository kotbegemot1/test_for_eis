from django.shortcuts import render
from django.http import HttpResponse
from .models import Accrual, Payment


# Create your views here.

list_delimiter = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)] # функция чтобы разделить список на список списков

def paided(request):
    paided = []
    not_paided = []
    ac = list(Accrual.objects.all()) # долги отсортированы в модели по дате
    pa = list(Payment.objects.all()) # платежи отсортированы в модели по дате
    n = 0
    while n!=len(ac)-1:
        for i in range(len(ac)):
            if ac[i] not in paided: # проверяем нет ли долга в списке оплаченных долгов
                try:
                    if ac[i].month == pa[0].month: # тут сравниваем платеж и долг по месяцу
                        paided.append(ac[i])
                        paided.append(pa[0])
                        ac.pop(i) # удаляем оплаченный долг из списка долгов
                        break
                except IndexError: # ловим исключение на случай если долгов больше чем платежей
                    break
        try:
            if pa[0] not in paided: # смотрим нет ли уже этого платежа в списке оплаченых долгов
                paided.append(ac[0])
                paided.append(pa[0])
                ac.pop(0) # удаляем оплаченный долг из списка долгов
        except IndexError: # ловим исключение на случай если долгов больше чем платежей
            break
        pa.pop(0) # удаляем исполненный платеж из списка  платежей
        n += 1
    paided = list_delimiter(paided, 2) #делим список на список списков по 2

    return render(request,'req/paided.html', context={'paided':paided, 'pa':pa, 'ac':ac})


def list_ac_pa(request):
    ac = list(Accrual.objects.all()) 
    pa = list(Payment.objects.all())
    return render(request, 'req/list.html', context={'ac':ac, 'pa': pa})

