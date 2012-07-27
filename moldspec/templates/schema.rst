{% from "common.rst" import renderSchema %}
{{ renderSchema(schema) }}


JSON Schema:

.. code-block:: javascript

{{ schema|prettyschema }}