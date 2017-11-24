|PythonPIP|_ |PythonSupport|_ |License|_ |RTFD|_

kairosdb - Python library to interface the KairosDB REST API (kairosdb.github.io)
=================================================================================

* *Author:* Denis 'jawa' Pompilio <denis.pompilio@gmail.com>
* *Contact:* Denis 'jawa' Pompilio <denis.pompilio@gmail.com>
* *Sources:* https://github.com/outini/python-kairosdb/

This package provides a simple python library to interface the KairosDB REST API.
Please read also: https://kairosdb.github.io/docs/build/html/restapi/index.html.

Installation
------------

To be documented

Documentation
-------------

Documentation is available online: http://python-kairosdb.readthedocs.io/en/latest/index.html

Examples
--------

.. code:: python

    import kairosdb

    if __name__ == "__main__":
        KDB_CLIENT = kairosdb.client.KairosDBAPIClient(
            api_endpoint="https://kdb.domain.tld:4443/api/v1")
        KDB_API = kairosdb.KairosDBAPI(KDB_CLIENT)

        print(KDB_API.version)
        print(KDB_API.health_status)
        print(KDB_API.health_check)
        print(KDB_API.metricnames)
        print(KDB_API.tagnames)

        print(KDB_API.query_metrics({
            "metrics": [{
                "name": "my_metric",
                "group_by": [{"name": "tag", "tags": ['host']}],
                "aggregators": [{
                    "name": "avg",
                    "align_sampling": True,
                    "sampling": {"value": 30, "unit": "seconds"}
                }]
            }],
            "cache_time": 0,
            "start_relative": {"value": "2", "unit": "hours"}
        })

License
-------

MIT LICENSE *(see LICENSE file)*

.. |PythonPIP| image:: https://badge.fury.io/py/python-kairosdb.svg
.. _PythonPIP: https://pypi.python.org/pypi/python-kairosdb/
.. |PythonSupport| image:: https://img.shields.io/badge/python-3.4+-blue.svg
.. _PythonSupport: https://github.com/outini/python-kairosdb/
.. |License| image:: https://img.shields.io/badge/license-MIT-green.svg
.. _License: https://github.com/outini/python-kairosdb/
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/
.. _Codacy: https://www.codacy.com/app/outini/python-kairosdb
.. |Coverage| image:: https://api.codacy.com/project/badge/Coverage/
.. _Coverage: https://www.codacy.com/app/outini/python-kairosdb
.. |RTFD| image:: https://readthedocs.org/projects/python-kairosdb/badge/?version=latest
.. _RTFD: http://python-kairosdb.readthedocs.io/en/latest/?badge=latest
