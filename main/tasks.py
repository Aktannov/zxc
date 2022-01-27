from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_order_mail(data):
    send_mail('Подтверждение о брони', f'Вы забронировали поход в музей на"дата,время"', 'test@gmail.com', [data.email])
