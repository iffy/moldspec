from twisted.python.filepath import FilePath
from jinja2 import Environment, FileSystemLoader

pkg_root = FilePath(__file__).parent()
doc_root = pkg_root.parent().child('docs')

env = Environment(loader=FileSystemLoader(pkg_root.child('templates').path))


def render(name, params):
    template = env.get_template(name)
    return template.render(params)


def renderTo(dst, name, params):
    dst.setContent(render(name, params))


def main():
    # non-resources
    schema_root = doc_root.child('schema')
    from moldspec.doc.fact import schema
    renderTo(schema_root.child('fact.rst'), 'schema.rst', {
        'schema': schema,
    })
    
    # resources
    schema_root = doc_root.child('resources')
    doctypes = ['identity', 'observation', 'prescription']
    
    from moldspec.doc.resource.files import schema
    for doctype in doctypes:
        doctype_schema = schema.get(doctype, None)
        if not doctype_schema:
            continue
        renderTo(schema_root.child('file.%s.rst' % doctype), 'schema.rst', {
            'schema': doctype_schema,
        })
