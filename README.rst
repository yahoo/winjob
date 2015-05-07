winjob
******************************
Parser for Windows Scheduled Task files

Build Status
============

.. image:: https://pypip.in/download/winjob/badge.svg
    :target: https://pypi.python.org/pypi/winjob/
    
.. image:: https://img.shields.io/pypi/v/winjob.svg
   :target: https://pypi.python.org/pypi/winjob

.. image:: https://img.shields.io/badge/python-2.7-blue.svg
    :target: https://pypi.python.org/pypi/winjob/

.. image:: https://img.shields.io/pypi/l/winjob.svg
    :target: https://pypi.python.org/pypi/winjob/

Installation
================

.. code-block::

    $ pip install winjob

.. code-block::
    $ python setup.py install

Usage
================
As a module:

.. code-block:: python

    >>> import winjob
    >>> fd = open('taskfile.job', 'r')
    >>> task = winjob.winjob.read_task(fd.read())
    >>> print task.parse()

On the command line:

.. code-block::
    $ winjob.py taskfile.job

More Information
================
* Free software: BSD license, see LICENSE.txt for details
* Documentation: https://winjob.readthedocs.org.

Code licensed under the BSD license. See LICENSE.txt
file for terms.
