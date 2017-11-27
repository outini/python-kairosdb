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

import logging
import fnmatch
from logging.handlers import SysLogHandler
from kairosdb import client


#: Current version of the package as :class:`str`.
VERSION = "0.2.0"

#: Basic logger for KairosDB interface module
LOG = None


def basic_logger():
    """Configure a basic logger for KairosDB interface

    :return: Logger object
    """
    if not LOG:
        logger = logging.getLogger('kairosdb')
        logger.setLevel(logging.DEBUG)

        fmt_syslog = logging.Formatter(
            '%(module)s %(processName)s %(levelname)s: %(message)s')
        fmt_stream = logging.Formatter(
            '%(processName)s %(levelname)s: %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fmt_stream)
        logger.addHandler(stream_handler)

        syslog_handler = SysLogHandler(address='/dev/log')
        syslog_handler.setFormatter(fmt_syslog)
        syslog_handler.setLevel(logging.INFO)
        logger.addHandler(syslog_handler)

        global LOG
        LOG = logger

    return LOG


class KairosDBAPI(client.KairosDBAPIEndPoint):
    """KairosDB API interface

    .. attribute:: version

        KairosDB version from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/Version.html

    .. attribute:: health_status

        KairosDB health status from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/Health.html

    .. attribute:: health_check

        KairosDB health check from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/Health.html

    .. attribute:: metricnames

        KairosDB metric names from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/ListMetricNames.html

    .. attribute:: tagnames

        KairosDB tag names from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/ListTagNames.html

    .. attribute:: tagvalues

        KairosDB tag values from API.

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/ListTagValues.html
    """

    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super(KairosDBAPI, self).__init__(*args, **kwargs)

        self._metricnames = None
        self._tagnames = None
        self._tagvalues = None

    @property
    def version(self):
        """KairosDB version"""
        return self._get('version').get('version')

    @property
    def health_status(self):
        """KairosDB health status"""
        return self._get('health/status')

    @property
    def health_check(self):
        """KairosDB health check"""
        return self._get('health/check')

    @property
    def metricnames(self):
        """Metric names"""
        if not self._metricnames:
            self._metricnames = self._get('metricnames').get('results')
        return self._metricnames

    @property
    def tagnames(self):
        """Tag names"""
        if not self._tagnames:
            self._tagnames = self._get('tagnames').get('results')
        return self._tagnames

    @property
    def tagvalues(self):
        """Tag values"""
        if not self._tagvalues:
            self._tagvalues = self._get('tagvalues').get('results')
        return self._tagvalues

    def search_metrics(self, matches, exclude_matches=None):
        """Search KairosDB metrics using glob matches

        :param list matches: List of glob matches
        :param list exclude_matches: List of glob matches for exclusions
        :return: Matched metric names as :func:`list`
        """
        x_metrics = []
        [x_metrics.extend(fnmatch.filter(self.metricnames, match))
         for match in exclude_matches]
        x_metrics = set(x_metrics)

        matched_metrics = []
        for match in matches:
            for metric in fnmatch.filter(self.metricnames, match):
                if metric not in x_metrics:
                    matched_metrics.append(metric)

        return matched_metrics

    def query_metrics(self, data):
        """Get metrics data points

        :param dict data: Data to post for query
        :return: Metric data points as :class:`dict`

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/QueryMetrics.html
        """
        return self._post('datapoints/query', data=data)

    def delete_metric(self, metric_name):
        """Delete a metric and all data points associated with the metric

        :param str metric_name: Name of the metric to delete

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/DeleteMetric.html
        """
        return self._delete('metric/%s' % metric_name)

    def delete_datapoints(self, data):
        """Delete metric data points

        :param dict data: Data to post for query

        .. seealso:: \
            https://kairosdb.github.io/docs/build/html/restapi/DeleteDataPoints.html
        """
        return self._post('datapoints/delete', data=data)
