from celery import shared_task
import time
import random
from django.conf import settings
from django.core.mail import send_mail


@shared_task(name="add_two_numbers")
def add(x, y):
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    res = x * (y * random.randint(3, 100))
    return res
