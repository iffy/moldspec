.. _document-observation:

Observation Document
====================

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


XXX include schema
