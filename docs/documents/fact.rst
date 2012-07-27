.. _document-fact:

Fact Document
=============

Fact documents describe the (relatively) immutable characteristics of a system.  They are returned by :ref:`Fact Checkers <actor-fact-checker>`.


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
