from validation.engine import Validator
from validation import validators

Validator.extend('bail', validators.bail)
Validator.extend('required', validators.req)
Validator.extend('num', validators.num)
Validator.extend('min', validators.min)
Validator.extend('max', validators.max)
