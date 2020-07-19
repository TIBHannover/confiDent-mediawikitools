from mwclient import Site
from typing import ClassVar


def site(host:str, path:str, scheme:str, username='', password='') -> ClassVar:
    site_ = Site(host=host, path=path, scheme=scheme)
    if username and password:
        site_.login(username=username, password=password)
    return site_


def edit(site_:ClassVar, page:str, content:str, append=False):
    page = site_.pages[page]
    if append is True:
        content += '\n\n' + page.text()
    page.edit(content)