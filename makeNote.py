# -*- coding: utf-8 -*

import re
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parseNotes(parseFile(argv[1]))


def parseFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        dict = {key: value for key, value in enumerate(file)}
    return dict

def parseNotes(dict = None):
    noteDict = {}
    for time in range(1, int(1+len(dict)/5)):
        time_date = re.findall(r'\d{4}年\d{1,2}月\d{1,2}日', dict[1+(time-1)*5])[0]
        selected_time = re.findall(r'\d{1,2}:\d{1,2}:\d{1,2}', dict[1+(time-1)*5])[0]
        title = (dict[(time-1)*5]).split()[0].strip()
        if title in noteDict:
            noteDict[title].append(time_date + ' ' + selected_time + '\n' + '> ' + dict[3+(time-1)*5] +'\n')
        else:
            noteDict[title] = [time_date + ' ' + selected_time + '\n' + '> ' + dict[3+(time-1)*5] +'\n']
    for key in noteDict:
        with open(key+'.md', 'a', encoding='utf-8') as note:
            for value in noteDict[key]:
                note.write(value)

if __name__ == "__main__":
    sys.exit(main())
