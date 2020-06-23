import json
import logging
import urllib2

from django.conf import settings
from django.contrib.auth import get_user_model
from djcelery import celery

log = logging.getLogger(__name__)

User = get_user_model()


@celery.task
def push_existing_users_to_hubspot():
    try:
        log.info('*******************************************')
        log.info('Starting pushing existing users to Hubpost')

        field_names = settings.HUBSPOT_CONTACT_FIELDS
        mapping_fields = settings.HUBSPOT_CONTACT_MAPPING_FIELDS
        users = User.objects.filter().values(*field_names)

        data_body = list()
        for user in users:
            properties = [{"property": mapping_fields[field], "value": user[field]} for field in field_names]

            data_body.append({
                "email": user["email"],
                "properties": properties
            })

        url = 'https://api.hubapi.com/contacts/v1/contact/batch?hapikey={0}'.format(settings.HUBSPOT_API_KEY)
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req, json.dumps(data_body))
        log.info("Done !!!")
        log.info('*******************************************')
    except Exception:
        log.exception('Error when pushing existing users to Hubpot', exc_info=True)
