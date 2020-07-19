from setuptools import setup
from pathlib import Path

README_path = Path.cwd() / 'README.md'
with open(README_path, 'r') as README_f:
    README = README_f.read()

setup(
    name='mediawikitools',
    version='0.1.0',
    packages=['mediawikitools', 'mediawikitools/wiki',
              'mediawikitools/utilities'],
    url='',
    license='MIT License', author='Andre Castro',
    author_email='andre.castro@tib.eu',
    description='A series of Python mwclient library wrappers, to perform '
                'actions in Mediawiki instances',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=['Programming Language :: Python',
        'Programming Language :: Python :: 3.7' ],
    keywords='mediawiki wikipedia',
    install_requires=['mwclient'],
)

