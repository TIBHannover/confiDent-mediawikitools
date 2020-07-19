import yaml
from pathlib import Path
from typing import Dict


def yaml2dict(path: str) -> Dict:
    with open(path, 'r') as yaml_f:
        yaml_content = yaml_f.read()
        yaml_dict = yaml.safe_load(yaml_content)
    return yaml_dict


def yaml_get_source(file_: str) -> Dict:
    # file in application root: mediawiki/
    path = Path.cwd()
    if '/mediawikitools/mediawikitools/' in str(path):
        path = Path(__file__).parent.parent.parent
        path_file = path / file_
    else:
        path_file = Path(Path.cwd()) / file_
    yamldict = yaml2dict(path_file)
    return yamldict


if __name__ == '__main__':
    yaml_get_source('wikidetails.yml')
