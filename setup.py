#
#    Cachet API python client and interface (python-kairosdb)
#
#    Copyright (C) 2017 Denis Pompilio (jawa) <denis.pompilio@gmail.com>
#
#    This file is part of python-kairosdb
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
from distutils.core import setup

if __name__ == '__main__':
    readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
    release = "0.2.0"

    setup(
        name="python-kairosdb",
        version=release,
        url="https://github.com/outini/python-kairosdb",
        author="Denis Pompilio (jawa)",
        author_email="denis.pompilio@gmail.com",
        maintainer="Denis Pompilio (jawa)",
        maintainer_email="denis.pompilio@gmail.com",
        description="KairosDB REST API python client and interface",
        long_description=open(readme_file).read(),
        license="MIT",
        platforms=['UNIX'],
        scripts=[],
        packages=['kairosdb'],
        package_dir={'kairosdb': 'kairosdb'},
        data_files=[('share/doc/python-kairosdb', ['README.rst', 'LICENSE'])],
        keywords=['api', 'metrics', 'timeseries', 'python', 'kairosdb'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: POSIX :: BSD',
            'Operating System :: POSIX :: Linux',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Developers',
            'Topic :: Utilities',
            'Topic :: System :: Monitoring'
            ]
        )
