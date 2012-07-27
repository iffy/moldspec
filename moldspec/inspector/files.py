"""
File inspector
"""

from zope.interface import implements
from twisted.internet import defer
from hashlib import sha1

import os, os.path
import grp
import pwd
import jsonschema

from mold.interface import IInspector
from mold.schema.files import schema



class Inspector:
    """
    I inspect the state of files.
    """
    
    implements(IInspector)
    
    
    def inspect(self, params):
        """
        Inspect the state of the file.
        
        @param params: A dictionary conforming to
            C{mold.schema.files.schema['inspection']}
        
        @rtype: Deferred
        @return: The result of the inspection.  A dictionary conforming to
            C{mold.schema.files.schema['observation']}.  Or an error if one
            was encountered.
        """
        try:
            jsonschema.validate(params, schema['inspection'])
        except Exception as e:
            return defer.fail(e)
        
        path = params['name']
        result = {
            'kind': 'file',
            'name': path,
        }

        result['exists'] = os.path.exists(path)
        if result['exists']:
            stat_info = os.stat(path)
            result['size'] = stat_info.st_size
            
            # XXX this will probably need to be optimized
            result['sha'] = sha1(open(path, 'rb').read()).hexdigest()
            
            result['group'] = grp.getgrgid(stat_info.st_gid)[0]
            result['user'] = pwd.getpwuid(stat_info.st_uid)[0]
            result['permissions'] = stat_info.st_mode & 0o777
        return defer.succeed(result)
