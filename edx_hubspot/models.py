import json
import logging

import urllib2
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import UserProfile

log = logging.getLogger(__name__)


@receiver(post_save, sender=UserProfile)
def push_user_to_hubspot(sender, **kwargs):
    if settings.ENABLE_HUBSPOT_INTEGRATION and settings.ENABLE_HUBSPOT_SEND_CONTACTS:
        try:
            if kwargs['created']:
                user_profile = kwargs['instance']
                url = 'https://api.hubapi.com/contacts/v1/contact?hapikey={0}'.format(settings.HUBSPOT_API_KEY)

                field_names = settings.HUBSPOT_CONTACT_FIELDS
                mapping_fields = settings.HUBSPOT_CONTACT_MAPPING_FIELDS

                data = {
                    "properties": [
                        {
                            "property": mapping_fields[field],
                            "value": getattr(user_profile.user, field) if hasattr(user_profile.user, field) else None
                        } for field in field_names
                    ]
                }

                req = urllib2.Request(url)
                req.add_header('Content-Type', 'application/json')

                response = urllib2.urlopen(req, json.dumps(data))
                log.info(response.read())
        except Exception:
            log.exception('Error when pushing user to Hubpot', exc_info=True)
