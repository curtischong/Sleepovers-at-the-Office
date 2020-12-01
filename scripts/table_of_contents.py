# The goal of this script is to generate the table of contents in the main README

from common import *

README_PATH = "../README.md"
START_OF_TABLE_OF_CONTENTS = "<!--START OF TABLE OF CONTENTS-->"
END_OF_TABLE_OF_CONTENTS = "<!--END OF TABLE OF CONTENTS-->"

table_of_contents_issue_template = "#{issue_number} [{title}](issues/{filename})"

def write_table_of_contents(table_of_contents):
    f = open(README_PATH, "w")
    f.write(table_of_contents)
    f.close()

def get_table_of_contents(files):
    table_of_contents = "\n\n" + START_OF_TABLE_OF_CONTENTS
    for f in reversed(files):
        table_of_contents += "\n\n"
        table_of_contents += table_of_contents_issue_template.format(
            issue_number = f.issue_number,
            title = f.title,
            filename = f.filename,
        )
    return table_of_contents

def get_readme_content():
    with open(README_PATH) as fn:
        old_readme = fn.read()

    readme_content = old_readme
    table_of_contents_idx = old_readme.find(START_OF_TABLE_OF_CONTENTS)

    if table_of_contents_idx == -1:
        return readme_content.strip()

    # We've generated the table of contents before. We should remove it
    readme_content = readme_content[:table_of_contents_idx]
    return readme_content.strip()

files = read_files()
table_of_contents = get_table_of_contents(files)
readme_content = get_readme_content()
content = readme_content + table_of_contents + "\n\n" + END_OF_TABLE_OF_CONTENTS
write_table_of_contents(content)