"""
Extract the schema from where it lives and make rst files in docs for them.

XXX this should be test driven
"""


from twisted.python import usage
from twisted.python.filepath import FilePath
from jinja2 import Environment, FileSystemLoader

root = FilePath(__file__).parent()



class Options(usage.Options):

    optFlags = [
        ['verbose', 'v', "Write rendered output to STDOUT"],
    ]

    optParameters = [
        ['destination', 'd', root.child('docs').child('resources').path,
            "Directory in which to dump the rst files"],
        ['template-root', 't', root.child('templates').path,
            "Template directory to be used for rendering the files."],
        ['identity-template', None, 'identity.rst',
            "Name of the template within `template-root` that will be used "
            "to render Identity document schemas"],
        ['observation-template', None, 'observation.rst',
            "Name of the template within `template-root` that will be used "
            "to render Observation schemas"],
        ['prescription-template', None, 'prescription.rst',
            "Name of the template within `template-root` that will be used "
            "to render Prescription schemas"],
    ]


def main():
    options = Options()
    options.parseOptions()
    
    loader = FileSystemLoader(options['template-root'])
    env = Environment(loader=loader)
    doctypes = ['identity', 'observation', 'prescription']
    templates = {}
    for doctype in doctypes:
        templates[doctype] = env.get_template(options['%s-template'%doctype])
    
    from moldspec.doc.resource.files import schema
    resource = 'file'
    dst = FilePath(options['destination'])
    if not dst.exists():
        dst.makedirs()
    for doctype in doctypes:
        d = dst.child('%s.%s.rst' % (resource, doctype))
        template = templates[doctype]
        d.setContent(template.render({
            'resource': resource,
            'doctype': doctype,
            'schema': schema.get(doctype, {})
        }))
        print 'wrote: %s' % d.path
        if options['verbose']:
            print d.getContent()



if __name__ == '__main__':
    main()
