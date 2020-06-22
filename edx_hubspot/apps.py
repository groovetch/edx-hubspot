"""
App configuration for edx_hubspot.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class PushUserToHubspotPluginConfig(AppConfig):
    """
    Push User To Hubspot Plugin configuration.
    """
    name = 'edx_hubspot'
    verbose_name = 'Push User To Hubspot Plugin'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
                'devstack': {'relative_path': 'settings.devstack_docker'},
            }
        }
    }
