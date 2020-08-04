from typing import List, Tuple
from datetime import datetime
from mediawikitools.__init__ import site


def read(page: str) -> Tuple[str, str]:
    page = site.pages[page]
    if page.exists:
        return page.text(), page.last_rev_time
    else:
        return None, None


def edit(page: str, content: str, append=False, newpageonly=False):
    """

    :param page:
    :param content:
    :param append:
    :param newpageonly:  if True edit only performed in not yet exiting pages
    :return:
    """
    page = site.pages[page]
    if newpageonly is True and page.exists:
        # def does nothin if only new pages can be written
        # and page already exists
        return
    if page.text():
        if append is True:
            content += '\n\n' + page.text()  # append to existing text
        page.edit(content)
    else:
        page.edit(content)


def unpack_ask_response(response):
    # printout is ordered dict
    # TODO: review code
    d = {}
    # import pdb; pdb.set_trace()
    printouts = response['printouts']
    page = response['fulltext']
    d['page'] = page
    for prop in printouts:
        p_item = response['printouts'][prop]
        for prop_val in p_item:
            if isinstance(prop_val, dict) is False:
                d[prop] = prop_val
            else:
                # if len(prop_val) > 0:
                props = list(prop_val.keys())
                if 'fulltext' in props:
                    val = prop_val.get('fulltext')
                elif 'timestamp' in props:
                    val = datetime.fromtimestamp(
                        int(prop_val.get('timestamp')))
                else:
                    val = list(prop_val.values())[0]
                d[prop] = val
    return(d)


def ask(query: str) -> List:
    results_ = []
    for answer in site.ask(query):
        printouts_dict = unpack_ask_response(answer)
        results_.append(printouts_dict)
    return results_


if __name__ == '__main__':
    # from datetime import datetime
    # now = datetime.now()
    # now = now.strftime('%Y.%m.%d-%H:%M')
    # edit(page='Test', content=f'Test {now}', append=False)

    # ASK
    # query is the same string as the ask code:
    # {{[[Category:Organizer]]|?Contact ...
    # but without {{ }}
    results = ask(query="[[Category:Organizer]]|?Contact|?Contact.Contact"
                        "Person|?Contact.Contact Email|limit=50|offset=0")
    print(results)
