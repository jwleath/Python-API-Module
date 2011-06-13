#!/usr/bin/env python

"""Python wrapper for an API."""

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

# Maybe modules should import their own API key.
from api_key import API_KEY


class API(object):
    """An example class for a Python API wrapper."""

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.base_url = ''
        self.output_format = None

    def call_api(self, directory, **kwargs):
        """
        A generic example api wrapping method. Other methods can use this
        method to interact with the API.
        """
        url_list = [self.base_url, '/%s' % directory]
        kwargs.update({'api_key': self.api_key})
        try:
            output_format = kwargs.pop('output_format')
        except KeyError:
            output_format = self.output_format
        params = urlencode(kwargs)
        url_list.extend(['?', params])
        url = ''.join(url_list)
        data = urlopen(url).read()
        return self._format_data(output_format, data)

    def _format_data(self, output_format, data):
        """Internal method to return formatted data to developer."""
        if output_format == 'json':
            # Turn JSON into a dictionary.
            return json.loads(data)
        return data
