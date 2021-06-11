def is_folder(path):
    if not path.count('.') > 0:
        return True
    else:
        return False


def is_file(path):
    if path.count('.') > 0:
        return True
    else:
        return False


def is_code(path):
    if path.count('.cpp') > 0 or path.count('.py') > 0:
        return True
    else:
        return False


def is_image(path):
    if path.count('.png') > 0 or path.count('.jpg') > 0:
        return True
    else:
        return False


def level(path):
    return path.count('/')

# Submission Successful! 5 out of 5 private test(s) passed.
