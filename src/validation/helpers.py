def get_size(val):
    pass


def isnumeric(val, vdt):
    if val.isdigit():
        return True and vdt.hasRule(['int','num'])
    else:
        try:
            return float(val) and vdt.hasRule(['int','num'])
        except Exception as e:
            return False

def isint(val, vdt):
    if val.isdigit():
        return True and vdt.hasRule(['int','num'])
    else:
        try:
            return int(val) and vdt.hasRule(['int','num'])
        except Exception as e:
            return False
