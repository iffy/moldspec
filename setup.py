from distutils.core import setup

setup(
    url='https://github.com/iffy/mold',
    author='Matt Haggard',
    author_email='haggardii@gmail.com',
    name='mold',
    version='0.1',
    packages=[
        'mold', 'mold.test',
        'mold.schema', 'mold.schema.test',
        'mold.script', 'mold.script.test',
    ],
    install_requires=[
        'Twisted>=10.2.0',
    ],
    scripts=[
        'bin/mold',
    ]
)