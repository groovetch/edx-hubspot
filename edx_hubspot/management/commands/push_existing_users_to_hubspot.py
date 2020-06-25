import logging

from django.conf import settings
from django.core.management import BaseCommand

from edx_hubspot.tasks import push_existing_users_to_hubspot

logger = logging.getLogger(__name__)
log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Push existing users to Hubspot'

    def handle(self, *args, **options):
        if settings.ENABLE_HUBSPOT_INTEGRATION and settings.ENABLE_HUBSPOT_SEND_CONTACTS:
            push_existing_users_to_hubspot.apply_async()
        else:
            raise Exception("This feature is disabled")
