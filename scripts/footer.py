# The goal of this script is to append the footer to every issue
# If a footer already exists, this file will delete and regenerate a footer for that issue

from common import *

FOOTER_START = "<!--START OF FOOTER-->"
FOOTER_END = "<!--END OF FOOTER-->"
def remove_footer(f):
    footer_idx = f.contents.find(FOOTER_START)
    if footer_idx > -1:
        f.contents = f.contents[:footer_idx]
    return f

NAVIGATION_LINK_SEPARATOR = "&nbsp;&nbsp;|&nbsp;&nbsp;"
START_OF_NAV_LINKS = "<!--START OF ISSUE NAVIGATION LINKS-->"
END_OF_NAV_LINKS = "<!--START OF ISSUE NAVIGATION LINKS-->"
footer = """

{footer_start}
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
{start_of_nav_links}
<p align="center">{navigation_links}</p>
{end_of_nav_links}
{footer_end}
"""


def get_naviation_link(f):
    return "<a href='{filename}'>#{issue_number}: {title}</a>".format(
        filename=f.filename,
        issue_number=f.issue_number,
        title=f.title,
    )

def append_footers(files):
    n = len(files)
    for i in range(n):
        navigation_links = ""
        if i > 0:
            navigation_links = get_naviation_link(files[i - 1])
        if i > 0 and i < n - 1:
            navigation_links += NAVIGATION_LINK_SEPARATOR
        if i < n - 1:
            navigation_links += get_naviation_link(files[i + 1])
        files[i].contents = files[i].contents.strip() # since every time we add the footer we also add whitespace
        files[i].contents += footer.format(footer_start=FOOTER_START, footer_end=FOOTER_END,
            start_of_nav_links=START_OF_NAV_LINKS, end_of_nav_links=END_OF_NAV_LINKS,
            navigation_links=navigation_links,
        )
    return files

def write_files(files):
    for file in files:
        f = open(ISSUES_DIR + file.filename, "w")
        f.write(file.contents)
        f.close()


files = read_files()
files = [remove_footer(f) for f in files]
files = append_footers(files)
write_files(files)
print("finished generating footer")