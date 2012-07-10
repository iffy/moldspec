file.prescription
-----------------




``exists`` **(required)**
    ``boolean``
    
    ``true`` if the file should exist, ``false`` if it should not exist



``kind`` **(required)**
    ``string`` matching ``"file"``
    
    Indicates that this is a file resource



``path`` **(required)**
    ``string``
    
    Absolute path name of file





``group``
    ``string``
    
    Name of the group owning the file



``owner``
    ``string``
    
    Name of the user owning the file



``permissions``
    ``integer``
    
    Octal permission bits for the file, e.g. ``0755``.  Since it's a decimal you will need to convert to octal if you want it in that format.

