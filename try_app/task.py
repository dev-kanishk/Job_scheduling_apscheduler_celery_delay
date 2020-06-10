from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep
from .models import EmailSchedule
# from demoapp.models import Widget


@shared_task()
def simple_task(pk):
    print(pk)
    
    if isinstance(pk,int):
        email = EmailSchedule.objects.get(pk = pk)
    else:
        email = EmailSchedule.objects.get(pk = pk[0])


    
    email.is_send = True
    email.save()
    
    
    print("successfully implemented schedule ")



    


