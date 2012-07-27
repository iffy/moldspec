.. _document-fact:

Fact Document
=============

Fact documents describe the (relatively) immutable characteristics of a system.


Schema
------

.. include:: /schema/fact.rst


Example
-------

.. code-block:: javascript

    {
        'os': {
            'kind': 'linux',
            'distro': 'ubuntu',
            'version': '12.10',
        },
    }
