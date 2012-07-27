from distutils.core import setup

setup(
    url='https://github.com/iffy/moldspec',
    author='Matt Haggard',
    author_email='haggardii@gmail.com',
    name='moldspec',
    version='0.1',
    packages=[
        'moldspec', 'moldspec.test',
        'moldspec.doc', 'moldspec.doc.test',
        'moldspec.doc.resource',
    ],
    package_data={
        'moldspec': ['templates/*'],
    },
    install_requires=[
        'Twisted>=10.2.0',
        'jsonschema',
        'Jinja2',
    ],
    scripts=[]
)
