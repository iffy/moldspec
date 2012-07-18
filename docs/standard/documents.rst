Documents
=========


Fact document
-------------

XXX


Identity document
-----------------

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


Observation document
--------------------

Observation documents describe the **actual** state of a resource.  Each resource type has its own schema for its *Observation documents*.  You can see the complete list of resource-specific *Observation documents* here XXX.

They are returned as the result of inspections.

For example, a ``file`` resource observation document might look like this:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/tmp/foo",
        "exists": true,
        "size": 3493,
        "sha": "c30a7f7531c41ec102fb5510d58166b502f68437",
        "user": "foo",
        "group": "bar",
        ...
    }


Prescription document
---------------------

Prescription documents describe the **desired** state of a resource.  Each resource type has its own schema for its *Prescription documents*.  You can see the complete list of resource-specific *Prescription documents* here XXX.

These documents are given to `Conformers`_ which make the changes necessary to match the prescription.

For example, if we want to make sure the file ``/tmp/foo`` does not exist, we could prescribe that with this document:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/tmp/foo",
        "exists": false
    }


