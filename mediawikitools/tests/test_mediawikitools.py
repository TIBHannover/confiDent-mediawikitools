import pytest
import string
from random import choice
from mediawikitools.__init__ import site
from mediawikitools.wiki import actions


def randstring(lenght=10):
    out = "".join([choice(list(string.ascii_letters)) for n in range(lenght)])
    return out


def test_site():
    major, minor, patch = site.version
    assert major == 1 and minor == 34


def test_user():
    assert len(site.username) > 0


def test_ask():
    # should only happen if SMW is installed. Use API find that
    response = actions.ask(query='[[Category:+]]')
    assert len(response) > 0


@pytest.mark.read
def test_readpage():
    content, lastedit = actions.read(page='Main_Page')
    print(content, lastedit)
    assert len(content) > 0


@pytest.mark.read
def test_reademptypage():
    randpage = randstring()
    content, lastedit = actions.read(page=randpage)
    print(content, lastedit)
    assert not content and not lastedit


@pytest.mark.write
def test_edit():
    rstring = randstring(10)
    pagename = 'Test'
    actions.edit(page=pagename,
                 content=f'Edit {rstring} by ~~~~',
                 summary='Testing overwriting',
                 append=False)
    content, lastedit = actions.read(page=pagename)
    assert rstring in content

    # Test append=True
    appendrstring = randstring(10)
    actions.edit(page=pagename,
                 content=f'Edit {appendrstring} by ~~~~',
                 summary='Testing appending',
                 append=True)
    content, lastedit = actions.read(page=pagename)
    assert appendrstring in content

    # Test write to existing page with newpageonly=True
    # nothing should be written
    newrstring = randstring(10)
    actions.edit(page=pagename,
                 content=f'Edit {newrstring} by ~~~~',
                 newpageonly=True)
    assert newrstring not in content
