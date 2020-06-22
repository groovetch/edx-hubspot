Push User To Hubspot Plugin
===========================

Features
--------

-  This plugin is to listening in UserProfile model's post\_save signal
   to push newly registered user to Hubspot contacts.

Installation
------------

Open edX devstack
~~~~~~~~~~~~~~~~~

-  Clone this repo in the src folder of your devstack.
-  Add Hubspot API key to lms settings

::

    HUBSPOT_API_KEY = '********************************'

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
