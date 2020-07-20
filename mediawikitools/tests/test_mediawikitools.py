from mediawikitools.__init__ import site
from mediawikitools.wiki import actions

def test_site():
    major, minor, patch = site.version
    assert major == 1 and minor == 34


def test_user():
    assert len(site.username) > 0


def test_ask():
    # should only happen if SMW is installed. Use API find that
    response = actions.ask(query='[[Category:+]]')
    assert len(response) > 0

