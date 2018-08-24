winjob
******************************
Parser for Windows Scheduled Task files.  This module will attempt to determine if the job file is in binary or xml
format and then create an object that contains attributes for all of the fields. Calling that object's parse method
will cause it to return a dictionary of those fields. When used from the command line it will output that dictionary
as a JSON object.

Build Status
============

.. image:: https://img.shields.io/pypi/dm/winjob.svg
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
    >>> fd = open('taskfile.job', 'rb')
    >>> task = winjob.winjob.read_task(fd.read())
    >>> print(task.parse())

On the command line:

.. code-block::

    $ winjob.py taskfile.job

More Information
================
* Free software: BSD license, see LICENSE.txt for details
