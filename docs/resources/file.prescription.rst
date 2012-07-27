





``content`` **(required)**
    ``string``
    
    URI or local absolute path to the file



``exists`` **(required)**
    ``boolean``
    
    ``true`` if the file should exist, ``false`` if it should not exist





``kind`` **(required)**
    ``string`` matching ``"file"``
    
    Indicates that this is a file resource



``name`` **(required)**
    ``string``
    
    Absolute path of file











``group``
    ``string``
    
    Name of the group owning the file







``owner``
    ``string``
    
    Name of the user owning the file



``permissions``
    ``integer``
    
    Octal permission bits for the file, e.g. ``0755``.  Since it's an integer you will need to convert to octal if you want it in that format.






JSON Schema:

.. code-block:: javascript

    {
        "type": "object", 
        "properties": {
            "content": {
                "required": true, 
                "type": "string", 
                "description": "URI or local absolute path to the file"
            }, 
            "kind": {
                "pattern": "file", 
                "required": true, 
                "type": "string", 
                "description": "Indicates that this is a file resource"
            }, 
            "group": {
                "type": "string", 
                "description": "Name of the group owning the file"
            }, 
            "name": {
                "required": true, 
                "type": "string", 
                "description": "Absolute path of file"
            }, 
            "exists": {
                "required": true, 
                "type": "boolean", 
                "description": "``true`` if the file should exist, ``false`` if it should not exist"
            }, 
            "owner": {
                "type": "string", 
                "description": "Name of the user owning the file"
            }, 
            "permissions": {
                "type": "integer", 
                "description": "Octal permission bits for the file, e.g. ``0755``.  Since it's an integer you will need to convert to octal if you want it in that format."
            }
        }
    }