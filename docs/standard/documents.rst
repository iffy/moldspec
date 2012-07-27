Documents
=========

Identity
--------

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


Fact
----

Fact documents describe the (relatively) immutable characteristics of a system.  These documents must conform to this schema:

XXX include schema

Here's an example fact document:

.. code-block:: javascript

    {
        'os': {
            'kind': 'linux',
            'distro': 'ubuntu',
            'version': '12.10',
        },
    }


Prescription
------------

Prescription documents describe the **desired** state of a resource.  Each resource type has its own schema for its *Prescription documents*.  You can see the complete list of resource-specific *Prescription documents* here XXX.

These documents are given to `Conformers`_ which make the changes necessary to match the prescription.

For example, if we want to make sure the file ``/tmp/foo`` does not exist, we could prescribe that with this document:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/tmp/foo",
        "exists": false
    }


XXX include schema

XXX The prescription is actually a list of Prescriptions.  Somehow, each one should be associated with which steps are a result of it and should be cast into buckets depending on step success/failure (note from notebook -- may overlap with steps document).


Observation
-----------

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


Steps
-----

Steps documents contain the steps a Performer needs to follow to bring about the desired state.

Steps documents reference 

XXX include schema


