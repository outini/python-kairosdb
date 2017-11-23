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


class KairosDBAPI(client.KairosDBAPIEndPoint):
    """KairosDB API interface
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
        """
        return self._post('datapoints/query', data=data)

    def delete_metric(self, metric_name):
        """Delete a metric and all data points associated with the metric

        :param str metric_name: Name of the metric to delete
        """
        self._delete('metric/%s' % metric_name)

    def delete_datapoints(self, data):
        """Delete metric data points

        :param dict data: Data to post for query
        """
        return self._post('datapoints/delete', data=data)
