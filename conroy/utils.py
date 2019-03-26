def truncate_ellipses(string, length):
    if len(string) > length:
        string = '{}...'.format(string[:length - 3])

    return string
