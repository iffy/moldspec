from twisted.trial.unittest import TestCase
from twisted.python.filepath import FilePath
import jsonschema
from jsonschema import validate

import grp
import pwd
import os

from mold.inspector.files import Inspector
from mold.schema.files import schema


class InspectorTest(TestCase):

    timeout = 1


    def test_dne(self):
        """
        A file that does not exist should have a minimal observation.
        """
        root = FilePath(self.mktemp())
        root.makedirs()
        
        i = Inspector()
        d = i.inspect({
            'kind': 'file',
            'path': root.child('foo').path,
        })
        
        def check(result):
            validate(result, schema['observation'])
            self.assertEqual(result['kind'], 'file')
            self.assertEqual(result['path'], root.child('foo').path)
            self.assertEqual(result['exists'], False)
            
        return d.addCallback(check)


    def test_exists(self):
        """
        A file that exists should have some useful attributes
        """
        root = FilePath(self.mktemp())
        root.makedirs()
        it = root.child('foo')
        it.setContent('foobar content')
        it.chmod(0777)
        
        # XXX this is a little WET
        stat_info = os.stat(it.path)
        user = pwd.getpwuid(stat_info.st_uid)[0]
        group = grp.getgrgid(stat_info.st_gid)[0]
        
        i = Inspector()
        d = i.inspect({
            'kind': 'file',
            'path': it.path,
        })
        
        def check(result):
            from hashlib import sha1
            validate(result, schema['observation'])
            self.assertEqual(result['kind'], 'file')
            self.assertEqual(result['path'], root.child('foo').path)
            self.assertEqual(result['exists'], True)
            self.assertEqual(result['size'], len('foobar content'))
            self.assertEqual(result['sha'], sha1('foobar content').hexdigest())
            self.assertEqual(result['group'], group)
            self.assertEqual(result['user'], user)
            self.assertEqual(result['permissions'], 0777)
            
        return d.addCallback(check)


    def test_badschema(self):
        """
        An exception should be raised if the input data doesn't conform to the
        inspection schema
        """
        i = Inspector()
        self.assertFailure(i.inspect({'foo': 'bar'}),
                           jsonschema.ValidationError)

