.. _document-identity:

Identity Document
=================

Identity documents uniquely describe a resource.  All identity documents for all resources conform to this schema:

XXX reference/include this from elsewhere (preferably the actual code) instead of typing it inline.

.. code-block:: javascript

    {
        "type": "object",
        "properties": {
            "kind": {
                "type": "string",
                "description": "Name of resource class"
            },
            "name": {
                "type": "string",
                "description": "Unique key identifying exactly one resource within a class"
            }
        }
    }

For example, the identity document for the ``/etc/hosts`` file looks like this:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/etc/hosts"
    }
