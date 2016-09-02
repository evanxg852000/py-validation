from validation import Validator


def main():
    inputs={'tes':'evance','age':18, 'experience':2}
    rules={'name':'req|bail', 'age': 'num|min:20','experience':'num|min:3'}
    validator=Validator.make(inputs, rules)
    
    if not validator.fails():
        print('Data validation passed!')
    else:
        for a, e in validator.errors():
            print(a,e, end='\n')


if __name__ == '__main__':
    main()
