def heading(string, indentation=1):
    if indentation < 1:
        indentation = 1
    elif indentation > 6:
        indentation = 6
    return indentation * '#' + ' ' + string
