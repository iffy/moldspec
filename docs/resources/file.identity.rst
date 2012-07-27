





``kind`` **(required)**
    ``string`` matching ``"file"``
    
    Indicates that this is a file resource



``name`` **(required)**
    ``string``
    
    Absolute path of file










JSON Schema:

.. code-block:: javascript

    {
        "type": "object", 
        "properties": {
            "kind": {
                "pattern": "file", 
                "required": true, 
                "type": "string", 
                "description": "Indicates that this is a file resource"
            }, 
            "name": {
                "required": true, 
                "type": "string", 
                "description": "Absolute path of file"
            }
        }
    }