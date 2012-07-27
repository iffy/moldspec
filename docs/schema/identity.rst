









``kind``
    ``string``
    
    Name of resource class



``name``
    ``string``
    
    Unique key identifying exactly one resource within a class






JSON Schema:

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