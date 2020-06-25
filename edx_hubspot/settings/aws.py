import logging

log = logging.getLogger(__name__)


def plugin_settings(settings):
    if hasattr(settings, 'HUBSPOT_FEATURES'):
        settings.ENABLE_HUBSPOT_INTEGRATION = settings.HUBSPOT_FEATURES.get("ENABLE_HUBSPOT_INTEGRATION", False)
        settings.ENABLE_HUBSPOT_SEND_CONTACTS = settings.HUBSPOT_FEATURES.get("ENABLE_HUBSPOT_SEND_CONTACTS", False)

        if settings.ENABLE_HUBSPOT_INTEGRATION:
            log.info("Enabled Hubspot Integration")

            try:
                settings.HUBSPOT_API_KEY = settings.HUBSPOT_FEATURES["HUBSPOT_API_KEY"]
            except KeyError:
                raise Exception("HUBSPOT_API_KEY is required as ENABLE_HUBSPOT_INTEGRATION is enabled")

            try:
                if settings.HUBSPOT_FEATURES["ENABLE_HUBSPOT_SEND_CONTACTS"]:
                    settings.HUBSPOT_CONTACT_FIELDS = settings.HUBSPOT_FEATURES["HUBSPOT_CONTACT_FIELDS"]
                    settings.HUBSPOT_CONTACT_MAPPING_FIELDS = settings.HUBSPOT_FEATURES["HUBSPOT_CONTACT_MAPPING_FIELDS"]
            except KeyError:
                raise Exception(
                    "HUBSPOT_CONTACT_FIELDS, HUBSPOT_CONTACT_MAPPING_FIELDS keys are required as ENABLE_HUBSPOT_SEND_CONTACTS is enabled")

        else:
            log.info("Disabled Hubspot Integration")
    else:
        log.info("Disabled Hubspot Integration")
