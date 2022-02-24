import json
import logging
import datetime

from django.utils import timezone

from main.models import RequestLog

logger = logging.getLogger(__name__)


class MyUtil(object):

    def __init__(self):
        logger.info("## MyUtil ##")
        print("*** init MyUtil()")

    def save_request(self, input, ip):
        c = RequestLog.objects.create(
            input=input,
            ip_address=ip,
        )
        return c.pk

    def save_response(self, id, output, response_code=0):
        c = RequestLog.objects.get(
            pk=id,
        )
        c.output = output
        c.response_code = response_code
        c.duration = (timezone.now() - c.created_at).seconds
        c.save()
        return c.pk
