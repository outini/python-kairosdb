# coding: utf-8
#
#  KairosDB REST API python client and interface (python-kairosdb)
#
#  Copyright (C) 2017 Denis Pompilio (jawa) <denis.pompilio@gmail.com>
#
#  This file is part of python-kairosdb
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the MIT License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  MIT License for more details.
#
#  You should have received a copy of the MIT License along with this
#  program; if not, see <https://opensource.org/licenses/MIT>.

import json
import requests
import logging
from functools import partial


logger = logging.getLogger(__name__)


class KairosDBAPIClient(object):
    """KairosDB API client

    It implements common HTTP methods GET, POST, PUT and DELETE
    This client is using :mod:`requests` package. Please see
    http://docs.python-requests.org/ for more information.

    :param bool verify: Control SSL certificate validation
    :param int timeout: Request timeout in seconds
    :param str api_endpoint: KairosDB API endpoint

    .. method:: get(self, path, data=None, **kwargs)

        Partial method invoking :meth:`~KairosDBAPIClient.request` with
        http method *GET*.

    .. method:: post(self, path, data=None, **kwargs)

        Partial method invoking :meth:`~KairosDBAPIClient.request` with
        http method *POST*.

    .. method:: put(self, path, data=None, **kwargs)

        Partial method invoking :meth:`~KairosDBAPIClient.request` with
        http method *PUT*.

    .. method:: delete(self, path, data=None, **kwargs)

        Partial method invoking :meth:`~KairosDBAPIClient.request` with
        http method *DELETE*.
    """
    def __init__(self, api_endpoint, verify=None, timeout=None):
        """Initialization method"""
        self.verify = verify
        self.timeout = timeout

        self.api_endpoint = api_endpoint

        self.request_headers = {
            'User-Agent': 'python-kairosdb',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        self.r_session = requests.Session()

        # Directly expose common HTTP methods
        self.get = partial(self.request, method='GET')
        self.post = partial(self.request, method='POST')
        self.put = partial(self.request, method='PUT')
        self.delete = partial(self.request, method='DELETE')

    def request(self, path, method, data=None, **kwargs):
        """Handle requests to API

        :param str path: API endpoint's path to request
        :param str method: HTTP method to use
        :param dict data: Data to send (optional)
        :return: Parsed json response as :class:`dict`

        Additional named argument may be passed and are directly transmitted
        to :meth:`request` method of :class:`requests.Session` object.
        """
        if not path.startswith('http://') and not path.startswith('https://'):
            url = "%s/%s" % (self.api_endpoint, path)
        else:
            url = path

        if data is None:
            data = {}

        response = self.r_session.request(method, url,
                                          data=json.dumps(data),
                                          headers=self.request_headers,
                                          timeout=self.timeout,
                                          verify=self.verify,
                                          **kwargs)

        if response.status_code == 204:
            return {
                'return_code': response.status_code,
                'status': 'success'
            }

        try:
            response_data = {'return_code': response.status_code}
            response_data.update(response.json())
            return response_data
        except ValueError:
            return {
                'return_code': response.status_code,
                'response': response.text
            }


class KairosDBAPIEndPoint(object):
    """KairosDB API endpoint

    This class do not provide convenience methods :meth:`get`, :meth:`post`,
    :meth:`put` and :meth:`delete`. Those methods should be implemented by
    subclasses.

    :param CachetAPIClient api_client: Cachet API client instance

    .. attribute:: api_client

        :class:`~client.CachetAPIClient` instance passed at instantiation.

    .. attribute:: _get

        Alias to :meth:`~CachetAPIClient.get` method of :attr:`api_client`
        instance.

    .. attribute:: _post

        Alias to :meth:`~CachetAPIClient.post` method of :attr:`api_client`
        instance.

    .. attribute:: _put

        Alias to :meth:`~CachetAPIClient.put` method of :attr:`api_client`
        instance.

    .. attribute:: _delete

        Alias to :meth:`~CachetAPIClient.delete` method of :attr:`api_client`
        instance.
    """
    def __init__(self, api_client):
        """Initialization method"""
        self.api_client = api_client
        self._get = api_client.get
        self._post = api_client.post
        self._put = api_client.put
        self._delete = api_client.delete
