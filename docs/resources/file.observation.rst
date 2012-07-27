





``exists`` **(required)**
    ``boolean``
    
    ``true`` if the file exists, ``false`` if it doesn't





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
    
    Octal permission bits for the file, e.g. ``0755``.  Since it's a decimal you will need to convert to octal if you want it in that format.



``sha``
    ``string``
    
    SHA1 hash of the file's contents as a hexadecimal string



``size``
    ``['integer', 'long']``
    
    Current file size in bytes






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
                "description": "``true`` if the file exists, ``false`` if it doesn't"
            }, 
            "sha": {
                "type": "string", 
                "description": "SHA1 hash of the file's contents as a hexadecimal string"
            }, 
            "owner": {
                "type": "string", 
                "description": "Name of the user owning the file"
            }, 
            "permissions": {
                "type": "integer", 
                "description": "Octal permission bits for the file, e.g. ``0755``.  Since it's a decimal you will need to convert to octal if you want it in that format."
            }, 
            "size": {
                "type": [
                    "integer", 
                    "long"
                ], 
                "description": "Current file size in bytes"
            }
        }
    }