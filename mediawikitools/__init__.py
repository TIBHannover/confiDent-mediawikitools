from mediawikitools.wiki import actions
from mediawikitools.utilities import file_utils


wikidetails = file_utils.yaml_get_source('wikidetails.yml')
site = actions.site(host=wikidetails['host'],
                    path=wikidetails['path'],
                    scheme=wikidetails['scheme'],
                    username=wikidetails['username'],
                    password=wikidetails['password'])
