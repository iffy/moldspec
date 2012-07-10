State Documents
===============

Each resource has three state documents:

    1. *Inspection* document - used to query for the current state of a
       resource.
    2. *Observation* document - used to describe the current state of a
       resource.
    3. *Prescription* document - used to describe the desired state of a
       resource.

All documents are JSON serializable and conform to resource-specific `Schema Definitions`_.


Schema Definitions
------------------

Here are the schema definitions for each resource:

.. toctree::
    :maxdepth: 2
    
    schema/file
