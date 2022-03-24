from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests
import json
from customers.models import (
    Customer,
)
from django_q.tasks import async_task
from dateutil.relativedelta import relativedelta

bot_token = settings.TELEGRAM_BOT_API

def send_telegram(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001778424010' + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

@receiver(post_save, sender=Customer)
def save_form(sender, instance, created, **kwargs):
    if created:
        whatsapp_text = "Нет"
        if instance.is_whatsapp:
            whatsapp_text = "Да"

        name = instance.name
        phone_number = instance.phone_number

        if instance.rent is not None:
            start_date = instance.rent.start_date.strftime("%Y-%m-%d %H:%M:%S")
            end_date = instance.rent.end_date.strftime("%Y-%m-%d %H:%M:%S")
            total_hours = relativedelta(instance.rent.end_date, instance.rent.start_date)
            location = instance.rent.location.name
            try:
                promo_code = instance.rent.promo_code.code
            except:
                promo_code = "Отсутствует"
            
            message = "Заявка №:%s \nДата начала: %s \nДата окончания: %s \nВремя аренды: %s \nМестоположение: %s \nПромо код: %s \nИмя клиента: %s \nТелефон: %s \nМожно звонить на ватсап: %s" % (instance.id, start_date, end_date,("Часы: %s | Минуты: %s" % (total_hours.hours, total_hours.minutes)), location, promo_code, name, phone_number, whatsapp_text)
            async_task('rents.signals.send_telegram', message)

        if instance.transfer is not None:
            start_date = instance.transfer.start_date.strftime("%Y-%m-%d %H:%M:%S")
            end_date = instance.transfer.end_date.strftime("%Y-%m-%d %H:%M:%S")
            total_hours = relativedelta(instance.transfer.end_date, instance.transfer.start_date)
            pick_up = instance.transfer.pick_up
            try:
                drop_off = instance.transfer.drop_off.name
            except:
                drop_off = "Отсутствует"
               
            try:
                promo_code = instance.transfer.promo_code.code
            except:
                promo_code = "Отсутствует"
            
            message = "Заявка №:%s \nДата начала: %s \nДата окончания: %s \nВремя аренды: %s \nМесто посадки: %s \nПункт назначения: %s  \nПромо код: %s \nИмя клиента: %s \nТелефон: %s \nМожно звонить на ватсап: %s" % (instance.id, start_date, end_date,("Часы: %s | Минуты: %s" % (total_hours.hours, total_hours.minutes)), pick_up, drop_off, promo_code, name, phone_number, whatsapp_text)
            async_task('rents.signals.send_telegram', message)
        