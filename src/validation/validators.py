from . import helpers


def bail(attr, val, vdt, *args):
    vdt.bail() #to bail
    return True

def req(attr, val, vdt, *args):
    if val is None or len(val) == 0 :
        vdt.errors().put(attr, 'The {} is required'.format(attr))
        return False
    return True

def num(attr, val, vdt, *args):
    if not helpers.isnumeric(val, vdt):
        vdt.errors().put(attr, 'The {} should be numeric'.format(attr))
        return False
    return True

def integer(attr, val, vdt, *args):
    if not helpers.isint(val, vdt):
        vdt.errors().put(attr, 'The {} should be an integer'.format(attr))
        return False
    return True

def min(attr, val, vdt, *args):
    if len(args) == 0:
        raise Exception("The min validator require one parameter.")

    if helpers.isint(val, vdt):
        if not(int(val) >= int(args[0])):
            vdt.errors().put(attr, 'The {} should be greater than or equal to {}'.format(attr,  args[0]))
            return False
    elif helpers.isnumeric(val, vdt):
        if not (float(val) >= int(args[0])):
            vdt.errors().put(attr, 'The {} should be greater than or equal to {}'.format(attr,  args[0]))
            return False
    else:
        if not(len(val) >= int(args[0])):
            vdt.errors().put(attr, 'The length of {} should be longer than or equal to {}'.format(attr,  args[0]))
            return False
    return True

def max(attr, val, vdt, *args):
    if len(args) == 0:
        raise Exception("The min validator require one parameter.")

    if helpers.isint(val, vdt):
        if not(int(val) <= int(args[0])):
            vdt.errors().put(attr, 'The {} should be less than or equal to {}'.format(attr,  args[0]))
            return False
    elif helpers.isnumeric(val, vdt):
        if not (float(val) <= int(args[0])):
            vdt.errors().put(attr, 'The {} should be less than or equal to {}'.format(attr,  args[0]))
            return False
    else:
        if not(len(val) <= int(args[0])):
            vdt.errors().put(attr, 'The length of {} should be shorter than or equal to {}'.format(attr,  args[0]))
            return False
    return True

def between(attr, val, vdt, *args):
    if len(args) < 2:
        raise Exception("The between validator require two parameters.")
    if helpers.isint(val, vdt):
        if not (int(val) >= int(args[0]) and int(val) <= int(args[1])):
            vdt.errors().put(attr, 'The {0} should be between {1} and {2}'.format(attr, args[0], args[1]))
            return False
    elif helpers.isnumeric(val, vdt):
        if not (float(val) >= int(args[0]) and int(val) <= int(args[1])):
            vdt.errors().put(attr, 'The {0} should be between {1} and {2}'.format(attr, args[0], args[1]))
            return False
    else:
        if not (len(val) >= int(args[0]) and len(val) <= int(args[1])):
            vdt.errors().put(attr, 'The length of {0} should be between {1} and {2}'.format(attr, args[0], args[1]))
            return False

    return True
