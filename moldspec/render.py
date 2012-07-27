from twisted.python.filepath import FilePath
from jinja2 import Environment, FileSystemLoader
import json

pkg_root = FilePath(__file__).parent()
doc_root = pkg_root.parent().child('docs')

env = Environment(loader=FileSystemLoader(pkg_root.child('templates').path))


def render(name, params):
    template = env.get_template(name)
    return template.render(params)


def renderTo(dst, name, params):
    dst.setContent(render(name, params))


def renderResourceSchema(name, schema):
    schema_root = doc_root.child('resources')
    doctypes = ['identity', 'observation', 'prescription']
       
    for doctype in doctypes:
        doctype_schema = schema.get(doctype, None)
        if not doctype_schema:
            continue
        renderTo(schema_root.child('%s.%s.rst' % (name,doctype)), 'schema.rst', {
            'schema': doctype_schema,
        })


def prettySchema(schema, indent=4):
    pretty = json.dumps(schema, indent=indent).split('\n')
    pretty = [' '*indent + x for x in pretty]
    return '\n'.join(pretty)

env.filters['prettyschema'] = prettySchema


def main():
    # non-resources
    schema_root = doc_root.child('schema')
    from moldspec.doc.fact import schema
    renderTo(schema_root.child('fact.rst'), 'schema.rst', {
        'schema': schema,
    })
    from moldspec.doc.identity import schema
    renderTo(schema_root.child('identity.rst'), 'schema.rst', {
        'schema': schema,
    })
    
    # resources
    from moldspec.doc.resource import files
    renderResourceSchema('file', files.schema)
