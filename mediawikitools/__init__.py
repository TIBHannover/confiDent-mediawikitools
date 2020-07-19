from mwclient import Site
from typing import ClassVar
from mediawikitools.utilities import file_utils


def login(host: str, path: str, scheme: str, username='', password='') -> \
        ClassVar:
    site_ = Site(host=host, path=path, scheme=scheme)
    if username and password:
        site_.login(username=username, password=password)
    return site_


wikidetails = file_utils.yaml_get_source('wikidetails.yml')
site = login(host=wikidetails['host'],
             path=wikidetails['path'],
             scheme=wikidetails['scheme'],
             username=wikidetails['username'],
             password=wikidetails['password'])
