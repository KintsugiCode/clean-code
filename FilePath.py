import re
import random

# log/cups/
def get_path_part(sFilename):
    if len(sFilename) > 0 and sFilename[len(sFilename) - 1] == '/':
        return sFilename

    try:
        #integer is index where the last slash is found
        integer = int(sFilename.rindex('/'))
    except:
        integer = -1

    dirName = ''
    if integer >= 0:
        dirName = sFilename[0: integer + 1]
    else:
        dirName = ''

    return dirName

# access_log
def getFilenamePart(sFilename):
    try:
        int(sFilename.rindex('/'))
    except:
        return sFilename

    pos = sFilename.rindex('/')
    base_name = sFilename[pos + 1:]
    return base_name


#.png
def getEndOfFile(sFilename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', sFilename)]
        return sFilename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_path_part("log/cups/access_log") == "log/cups/")
assert(get_path_part("log/cups/") == "log/cups/")
assert(get_path_part("cups/access_log") == "cups/")
assert(get_path_part("access_log") == "")
assert(getFilenamePart("log/cups/access_log") == "access_log")
assert(getFilenamePart("log/cups/") == "")
assert(getFilenamePart("cups/access_log") == "access_log")
assert(getFilenamePart("access_log") == "access_log")
assert(getEndOfFile("log/cups/access_log") == "")
assert(getEndOfFile("base/FileHelper.cpp") == "cpp")
assert(getEndOfFile("base/FileHelper.cpp.bak") == "bak")