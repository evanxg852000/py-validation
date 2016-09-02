from validation.engine import Validator
from validation import validators

Validator.extend('bail', validators.bail)
Validator.extend('req', validators.req)
Validator.extend('num', validators.num)
Validator.extend('int', validators.integer)
Validator.extend('min', validators.min)
Validator.extend('max', validators.max)
Validator.extend('btw', validators.between)
