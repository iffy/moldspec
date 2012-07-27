Observation
-----------




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

