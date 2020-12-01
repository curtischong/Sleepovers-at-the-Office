import os
import glob
from operator import attrgetter

ISSUES_DIR = "../issues/"
class File:
    path = ''
    filename = ''
    issue_number = 0
    contents = ''
    title = ''
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.issue_number = self.__get_issue_number()
        with open(path) as fn:
            self.contents = fn.read()
            self.title = self.__get_title()

    def __get_issue_number(self):
        code = self.filename[:3]
        # get rid of leading 0s
        for i in range(len(code)):
            if code[i] != '0':
                return code[i:]
        return -1

    def __get_title(self):
        title = self.contents.split("\n")[0] # get the first line
        return title[2:] # remove the "# "

def read_files():
    files = []
    for path in glob.glob(ISSUES_DIR + "*"):
        f = File(path)
        files.append(f)
    return sorted(files, key=attrgetter("filename"))