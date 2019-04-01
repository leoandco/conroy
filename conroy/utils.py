import re


def truncate_ellipses(string, length):
    if len(string) > length:
        string = '{}...'.format(string[:length - 3])

    return string


def truncate_newline(string):
    return next(x for x in re.split(r'[\r\n]', string) if x)
