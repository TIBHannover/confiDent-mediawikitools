from setuptools import setup
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
    install_requires=['mwclient'],
)

