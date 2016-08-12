poi.maildefaults Overview
=========================

The ``poi.maildefaults`` add-on for Plone works with the `poi.recievemail <https://github.com/sixfeetup/poi.receivemail>`_ fork that has support for setting default values for fields that would normally be required if you were submitting the issue TTW. Currently it is very basic and doesn't do much validation of the values which means your Poi Issues could be invalid and not be created if you put in an incorrect value.

Installation
============

Just add ``poi.maildefaults`` to your eggs in your buildout and install it via the "Plone Add-Ons" control panel. Once you do, you will now have a "Mail Defaults" tab on your Poi Trackers.

