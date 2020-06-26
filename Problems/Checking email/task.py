def check_email(string):
    if string.count(' ') > 0:
        return False
    if string.count('@') != 1:
        return False
    if string[string.find('@') + 1] == '.':
        return False
    if string.find('.', string.find('@')) == -1:
        return False
    return True

