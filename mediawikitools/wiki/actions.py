from mediawikitools.__init__ import site


def edit(page: str, content: str, append=False):
    print(site)
    page = site.pages[page]
    if append is True:
        content += '\n\n' + page.text()
    page.edit(content)


if __name__ == '__main__':
    from datetime import datetime
    now = datetime.now()
    now = now.strftime('%Y.%m.%d-%H:%M')
    edit(page='Test', content=f'Test {now}', append=False)
