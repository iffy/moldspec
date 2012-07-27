.. _document-prescription:

Prescription Document
=====================

Prescription documents describe the **desired** state of a resource.  Each resource type has its own schema for its Prescription documents.  You can see the complete list of resource-specific Prescription documents here XXX.

These documents are given to a :ref:`actor-performer` which make the changes necessary to match the prescription.

For example, if we want to make sure the file ``/tmp/foo`` does not exist, we could prescribe that with this document:

.. code-block:: javascript

    {
        "kind": "file",
        "name": "/tmp/foo",
        "exists": false
    }


XXX The prescription is actually a list of Prescriptions.  Somehow, each one should be associated with which steps are a result of it and should be cast into buckets depending on step success/failure (note from notebook -- may overlap with steps document).


