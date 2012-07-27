





``kind`` **(required)**
    ``string`` matching ``"user"``
    
    Indicates that this is a user resource



``name`` **(required)**
    ``string``
    
    Name of user










JSON Schema:

.. code-block:: javascript

    {
        "type": "object", 
        "properties": {
            "kind": {
                "pattern": "user", 
                "required": true, 
                "type": "string", 
                "description": "Indicates that this is a user resource"
            }, 
            "name": {
                "required": true, 
                "type": "string", 
                "description": "Name of user"
            }
        }
    }