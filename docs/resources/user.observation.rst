







``exists`` **(required)**
    ``boolean``
    
    true if the user exists; false if it doesn't







``kind`` **(required)**
    ``string`` matching ``"user"``
    
    Indicates that this is a user resource



``name`` **(required)**
    ``string``
    
    Name of user









``comment``
    ``string``
    
    A description of the user





``gid``
    ``string``
    
    User's group ID or name



``home``
    ``string``
    
    Path to user's home







``password``
    ``string``
    
    Password hash



``shell``
    ``string``
    
    Path to the shell for user



``uid``
    ``string``
    
    User's user ID






JSON Schema:

.. code-block:: javascript

    {
        "type": "object", 
        "properties": {
            "comment": {
                "type": "string", 
                "description": "A description of the user"
            }, 
            "kind": {
                "pattern": "user", 
                "required": true, 
                "type": "string", 
                "description": "Indicates that this is a user resource"
            }, 
            "shell": {
                "type": "string", 
                "description": "Path to the shell for user"
            }, 
            "name": {
                "required": true, 
                "type": "string", 
                "description": "Name of user"
            }, 
            "exists": {
                "required": true, 
                "type": "boolean", 
                "description": "true if the user exists; false if it doesn't"
            }, 
            "gid": {
                "type": "string", 
                "description": "User's group ID or name"
            }, 
            "home": {
                "type": "string", 
                "description": "Path to user's home"
            }, 
            "password": {
                "type": "string", 
                "description": "Password hash"
            }, 
            "uid": {
                "type": "string", 
                "description": "User's user ID"
            }
        }
    }