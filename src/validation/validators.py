  
def bail(attr, val, vdt, *args):  
    vdt.bail() #to bail
    return True
    
def req(attr, val, vdt, *args):  
    if len(val)==0 :
        vdt.errors().put(attr, 'The {} is required'.format(attr))
        return False
    return True

def num(attr, val, vdt, *args):
    if not str(val).isdigit():
        vdt.errors().put(attr, 'The {} should be numeric'.format(attr))
        return False
    return True 

def min(attr, val, vdt, *args):
    if len(args) == 0:
        raise Exception("The min validator require one parameter.") 
    if val < int(args[0]) :
        vdt.errors().put(attr, 'The {} should be more than or equal to {}'.format(attr,  args[0]))
        return False
    return True

def max(attr, val, vdt, *args):  
    if len(args) == 0:
        raise Exception("The max validator require one parameter.") 
    if val > int(args[0]) :
        vdt.errors().put(attr, 'The {} should be less than or equal to {}'.format(attr,  args[0]))
        return False
    return True

