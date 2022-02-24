import json
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailUtil(object):

    def __init__(self):
        logger.info("## EmailUtil ##")
        print("*** init EmailUtil()")

    def send_generic_email(self):
        pass

    def send_contact_email(self, contact):
        logger.info("## send contact email ##")
        try:
            headers = {
                "Authorization": f"Bearer {settings.SENDGRID_TOKEN}",
                "Content-Type": "application/json"
            }
            data = {
                "personalizations": [
                    {
                        "to": [{"email": settings.OWNER_EMAIL}]
                    }
                ],
                "from": {"email": f"Bella Books Contact <{settings.ADMIN_EMAIL}>"},
                "subject": f"Bella Books Contact Form: {contact.email}",

                "content": [
                    {
                        "type": "text/plain",
                        "value": "Test test test!"
                    },
                    {
                        "type": "text/html",
                        "value": f"""
                    <html>
                        <head>
                            <title>Bella Books Contact Form</title>
                        </head>
                        <body>
                            <h1>Contact Added!</h1>
                            <table>
                            <tr><td>Email</td><td>Mobile number</td><td>Name</td></tr>
                            <tr><td>{contact.email}</td><td>{contact.mobile_number}</td>
                            <td>{contact.name}</td></tr>
                            </table>
                            <h2>Message</h2>
                            <p>{contact.message}</p>
                        </body>
                    </html>
                    """
                    }
                ]
            }
            r = requests.post(url=settings.SENDGRID_URL,
                              headers=headers,
                              data=json.dumps(data))
            logger.info(r)
        except Exception as e:
            logger.error(e)

    def send_order_email(self, _to, _from, _subject, _message):
        logger.info("## send order email ##")
        print("## send order email ##")
        try:
            headers = {
                "Authorization": f"Bearer {settings.SENDGRID_TOKEN}",
                "Content-Type": "application/json"
            }
            data = {
                "personalizations": [
                    {
                        "to": [{"email": _to}],
                        "bcc": [{"email": settings.OWNER_EMAIL}]
                    }
                ],
                "from": {"email": f"Bella Books <{_from}>"},
                "subject": _subject,
                "content": [
                    {
                        "type": "text/plain",
                        "value": _message
                    },
                    {
                        "type": "text/html",
                        "value": _message
                    }
                ]
            }
            print(json.dumps(data))
            r = requests.post(url=settings.SENDGRID_URL,
                              headers=headers,
                              data=json.dumps(data))
            logger.info(r)
            print(r)
        except Exception as e:
            logger.error(e)