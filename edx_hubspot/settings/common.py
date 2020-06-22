import logging

log = logging.getLogger(__name__)


def plugin_settings(settings):
    settings.ENABLE_LMS_HUBSPOT_INTEGRATION = settings.FEATURES.get("ENABLE_LMS_HUBSPOT_INTEGRATION", False)

    if settings.ENABLE_LMS_HUBSPOT_INTEGRATION:
        log.info("Enabled LMS Hubspot Integration")

        try:
            settings.HUBSPOT_API_KEY = settings.HUBSPOT_API_KEY
        except Exception as e:
            raise Exception("HUBSPOT_API_KEY key required as ENABLE_LMS_HUBSPOT_INTEGRATION is enabled")
    else:
        log.info("Disabled LMS Hubspot Integration")
