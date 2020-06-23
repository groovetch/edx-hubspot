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

-  Clone this repo in the src folder of your devstack.
-  Add Hubspot API key to lms settings

::
    FEATURES['ENABLE_LMS_HUBSPOT_INTEGRATION'] = True
    HUBSPOT_API_KEY = '********************************'
    HUBSPOT_CONTACT_FIELDS = ["email", "first_name", "last_name"] // list of user fields to push to Hubspot
    HUBSPOT_CONTACT_MAPPING_FIELDS = {"email": "email", "first_name": "firstname", "last_name": "lastname"} // fields mapping due to the different of naming conventions between django and Hubspot

-  Open a new LMS shell.
-  Install the plugin as follows: pip install -e
   git+https://github.com/groovetch/edx-hubspot.git#egg=edx-hubspot
-  Restart Lms services.

Usage
-----

Include a usage description for your plugin.

Contributing
------------

Add your contribution policy. (If required)
