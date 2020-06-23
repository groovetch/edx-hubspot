Push User To Hubspot Plugin
===========================

Features
--------

-  This plugin is to listening in UserProfile model's post_save signal
   to push newly registered user to Hubspot contacts.

Installation
------------

Open edX devstack
~~~~~~~~~~~~~~~~~

-  Install this repository: pip install -e git+https://github.com/groovetch/edx-hubspot.git#egg=edx_hubspot
-  Add LMS settings

.. code:: bash

    // enable EDX Hubspot Integration
    ENABLE_LMS_HUBSPOT_INTEGRATION = True

    // Hubspot API key
    HUBSPOT_API_KEY = "******************"

    // list of user fields to push to Hubspot contacts
    HUBSPOT_CONTACT_FIELDS = ["email", "first_name", "last_name"]

    // field mapping settings due to the differences of field naming convention between Django and Hubspot
    HUBSPOT_CONTACT_MAPPING_FIELDS = {"email": "email", "first_name": "firstname", "last_name": "lastname"}

- Restart LMS server

Usage
-----

Include a usage description for your plugin.

Contributing
------------

Add your contribution policy. (If required)
