# Usage:
# 1) Create a file xxx_an_issue_title.md
# 2) On the first line, put a # and write the title
# 3) Then fill in the rest of the issue with your markdown
# 4) Run make generate-issue and this script will:
#    i)  Generate the issue footer
#    ii) Generate a hyperlink to the issue on the main readme of this repo.
generate-issue:
	python3 scripts/footer.py && python3 scripts/table_of_contents.py