from celery import shared_task
from . import funcs

@shared_task
def hour_sync():
    funcs.send_xml_request()
