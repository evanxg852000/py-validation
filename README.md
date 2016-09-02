# Py validation

Py-validation is an easy to use python validation library. It implements the laravel framework validation syntaxe.

### About

Comming from the php community, I have a great experience in web app developement and many environments and platforms (Android, .NET Desktop, Javascript ). I love to use solutions from other framework or platforms to make my life easier. I really love approaching other plateforms as it has tougth me a lot on how should I approach a design or implementation problem. I usually find myself implementing javascript paterns in php because it makes more sense and straiforward.

I found myself in python projects lately, as I dug to find tools for validation, I found Cerberus which is really great. however I found that laravel validation is more convenient and less combersome for an experienced php developer like me. Thus I decided to roll my python validation library using the concepts from [laravel](https://laravel.com/docs/5.2/validation).

### Installation

Just download the src and import into your project. 
Please bear in mind that the validators are yet to be implemented so just use this to try the validation engine and its syntaxe.
The validators will be build allong the way ... You can also help in developing validators

### How to use it ?

```python
from validation import Validator

def main():
    inputs={'name':'evance','age':18, 'experience':2}
    rules={'name':'required', 'age': 'num|min:20','experience':'num|min:3'}
    validator=Validator.make(inputs, rules)
    if not validator.fails():
        print('Data validation passed!')
    else:
        for a, e in validator.errors():
            print(a,e, end='\n')

if __name__ == '__main__':
    main()
```

On execution, this will output 
```sh
experience ['The experience should be more than or equal to 3']
age ['The age should be more than or equal to 20']
```

### Validations 

Currently we have only five basic validations :
* bail :this special validator will make the engine skip the remaining rules on the current field being validated as soon as a the data fails one. this is useful if you just want to know that the data is valid  
* req : the input should not be empty, None -it is required
* num :the  input should be a numeric (float or integer)
* min :the input should be a digit greater than the min param [min:3] or a string longer than the min param [min:3]
* max :the input should be a digit less than the max param [max:5] or a string shorter than the min param [min:3]
* btw : the input should be a digit between the btw param [btw:3,5] or a string of length between the btw param [btw:3,5]

### Adding your own validation
You can extend the engine to add your own validators. the example below shows an example of this...

```sh
def evance(attr, val, vdt, *args):  
    if not val == "evance" :
        vdt.errors().put(attr, "The value of {} should be 'evance' ".format(attr))
        return False
    return True

Validator.extend('evance', evance)
```
Validation extend takes the name of the validator and a callable function as arguments. The function will be passed the following arguments when the engine calls the validator function :
* attr : (attribute) the input field under validation
* val : (value) the value of the input field during data submission
* vdt : (validator) the validator insatance you can use to add errors to the error bag
* *args : arguments your validator expect "max:5" for instance will have arg[0] as 5 

### Todos

 - Write solid & better validators  (regex)
 - Write unit Tests

### Reference 
Please peek at the laravel validation document [https://laravel.com/docs/5.2/validation]
