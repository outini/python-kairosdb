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

from kairosdb import client


#: Current version of the package as :class:`str`.
VERSION = "0.1.0"


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
        return self._get('metricnames').get('results')

    @property
    def tagnames(self):
        """Tag names"""
        return self._get('tagnames').get('results')

    @property
    def tagvalues(self):
        """Tag values"""
        return self._get('tagvalues').get('results')

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
