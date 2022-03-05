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

bot_token = settings.TELEGRAM_BOT_API

def send_telegram(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=-1001778424010' + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

@receiver(post_save, sender=Customer)
def save_form(sender, instance, created, **kwargs):
    if created:
        start_date = instance.rent.start_date
        end_date = instance.rent.end_date
        location = instance.rent.location.name
        try:
            promo_code = instance.rent.promo_code.code
        except:
            promo_code = "Отсутствует"
        
        whatsapp_text = "Нет"
        if instance.is_whatsapp:
            whatsapp_text = "Да"

        name = instance.name
        phone_number = instance.phone_number

        message = "Заявка №:%s \nДата начала: %s \nДата окончания: %s \nМестоположение: %s \nПромо код: %s \nИмя клиента: %s \nТелефон: %s \nМожно звонить на ватсап: %s" % (instance.id, start_date, end_date, location, promo_code, name, phone_number, whatsapp_text) 
        
        async_task('rents.signals.send_telegram', message)
        