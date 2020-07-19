from mediawikitools.__init__ import site


def test_site():
    major, minor, patch = site.version
    assert major == 1 and minor == 34


def test_user():
    assert len(site.username) > 0
