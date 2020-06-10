from django.shortcuts import render
from .task import simple_task
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import EmailSchedule 


# Create your views here.


def simple_test_view(request):
    print("Executing simple_test_view...")

    exec_time = datetime.utcnow() + timedelta(minutes=.5,hours=5.5)
    email = EmailSchedule.objects.create(exec_time=exec_time)
    pk = (email.pk,)
    start(pk)
    print(exec_time)
    # send_mail_task.apply_async((pk),eta=exec_time)
    print("called the simple_Task function successfully")
    return HttpResponse("view executed")


from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Calcutta'})
scheduler.start()

pending_emails = EmailSchedule.objects.filter(is_send=False)
for x in pending_emails:
    exec = datetime.utcnow()+timedelta(hours=5.5,minutes=0)
    print("resending",x.pk)    
    scheduler.add_job(simple_task, trigger='date', next_run_time=exec, args=[x.pk])




def start(pk):
    
    # print(exec_time)
    exec = datetime.utcnow()+timedelta(hours=5.5,minutes=1)    
    scheduler.add_job(simple_task.delay, trigger='date', next_run_time=exec, args=[pk,])