.. _document-identity:

Identity Document
=================

Identity documents uniquely identify a resource.

Schema
------

.. include:: /schema/identity.rst

Example
-------

For example, the identity document for the ``/etc/hosts`` file looks like this:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/etc/hosts"
    }
