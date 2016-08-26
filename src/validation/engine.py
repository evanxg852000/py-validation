
class Singleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Validators(object, metaclass=Singleton):
    _validators=None
        
    def __init__(self):
        self._validators={}

    def add(self, name, func):
        if callable(func):
            self._validators[str(name)]=func
        else:
            raise Exception(str(name), 'Is not a callable validator function.')
    
    def get(self, name):
        return self._validators[name] if name in self._validators else None
        

class ErrorBag(object):
    _errors=None
    # example {'attr':['min should be 5', 'max should be 10']}
    
    def __init__(self):
        self._errors={}
        
    def __iter__(self):
        for k,v in self._errors.items():
            yield k,v
        
    def put(self, attr, msg):
        if attr not in self._errors:
            self._errors[str(attr)]=[]           
        self._errors[str(attr)].append(msg)
            
            
    def hasError(self, attr):
        return (str(attr) in self._errors)
        
    
    def get(self, attr=None):
        return self._errors if attr == None else self._errors[str(attr)]  


class Validator():
    _validators=None
    _rules=[]
    _inputs={}
    _bail=False
    _errors=None
    
    def __init__(self, inputs, rules):
        self._validators=Validators()
        self._inputs=inputs
        self._rules=rules
        self._errors=ErrorBag()
        
    def _parse(self, ruleset):
        rules=[]
        items=ruleset.split('|')
        for item in items:
            code=item.split(':')
            if len(code) == 1 :
                rule=dict({'func': code[0], 'args': []})
            if len(code) > 1 :
                args=code[1].split(',')
                rule=dict({'func': code[0], 'args': args})
            rules.append(rule)
        return rules
        
        
    def bail(self):
        self._bail=True
        
    def fails(self):
        fails=False
        for name, ruleset in self._rules.items():
            ruleset=self._parse(ruleset)
            for rule in ruleset:
                func=self._validators.get(rule['func'])
                if not callable(func):
                    raise Exception("Undefined validator: {} ".format(rule['func']))
                value= self._inputs[name] if (name in self._inputs) else None
                ok=func(name, value, self, *rule['args'])
                if not ok :
                    fails=True
                    
            if self._bail:
                return fails
        return fails
            
                
        #implement core functionality here
    
    def errors(self):
        return self._errors
    
    
    @staticmethod
    def extend(name, func):
        Validators().add(name, func)
        
    @staticmethod
    def make(inputs, rules):
        return Validator(inputs, rules)

