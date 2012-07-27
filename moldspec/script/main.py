"""
Main entry point for `mold` command line tool.
"""

from __future__ import print_function

from twisted.python import usage
from twisted.internet import reactor
import json


class InspectOptions(usage.Options):

    synopsis = 'resource_type name'

    def parseArgs(self, kind, name):
        self['kind'] = kind
        self['name'] = name


def inspect(options, suboptions):
    def printit(result):
        print(json.dumps(result, sort_keys=True, indent=4))
        reactor.stop()
    if suboptions['kind'] == 'file':
        from mold.inspector.files import Inspector
        i = Inspector()
        return i.inspect({'kind': suboptions['kind'],
                          'name': suboptions['name']}).addBoth(printit)
    else:
        raise ValueError('Unknown resource type: %r' % suboptions['kind'])


class Options(usage.Options):

    subCommands = [
        ['inspect', 'i', InspectOptions, "Inspect the state of a resource"],
    ]


def main():
    """
    XXX
    """
    from twisted.internet import reactor
    options = Options()
    options.parseOptions()
    if options.subCommand == 'inspect':
        reactor.callWhenRunning(inspect, options, options.subOptions)
        reactor.run()

