# Mediawiki Tools

## wikidetails.yml & Write access:
Ensure user account belongs to bot group: see wiki page `Special:UserRights`

Create a bot password in wiki page: `Special:BotPasswords`

copy `wikidetails.template.yml` as `wikidetails.yml` and fill in bot name and password:<br/>
`cp wikidetails.template.yml wikidetails.yml`

## Use as Python package in another application/script
### Generate distribution packages
`python setup.py bdist_wheel`

### Import as package, in another script
`pip install path/to/mediawikitools/dist/mediawikitools-0.1.0-py3-none-any.whl`

Ensure: `wikidetails.yml` is in the root dir of the new script 

```python
from mediawikitools.wiki import actions
actions.edit(page='Test', content='test from another script')
```


## run tests
`tox`
will run tests and detect flake8s

`python -m pytest`
will only run the tests/test*.py

`flake8 somefile`
lint checks
