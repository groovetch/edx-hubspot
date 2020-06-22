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
    try:
        if kwargs['created']:
            user_profile = kwargs['instance']
            url = 'https://api.hubapi.com/contacts/v1/contact?hapikey={0}'.format(settings.HUBSPOT_API_KEY)
            data = json.dumps({
                "properties": [
                    {
                        "property": "email",
                        "value": user_profile.user.email
                    }
                ]
            })

            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')

            response = urllib2.urlopen(req, data)
            # log response here
    except Exception as e:
        log.exception("Error when pushing user to Hubspot", e)
