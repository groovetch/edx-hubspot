"""
App configuration for push_user_to_hubspot_plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class PushUserToHubspotPluginConfig(AppConfig):
    """
    Push User To Hubspot Plugin configuration.
    """
    name = 'push_user_to_hubspot_plugin'
    verbose_name = 'Push User To Hubspot Plugin'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
                'devstack': {'relative_path': 'settings.docker_devstack'},
            }
        }
    }
