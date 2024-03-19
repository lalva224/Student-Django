from django.core.exceptions import ValidationError
import re

def validate_name_format(value):
    """
    Validator for the "First M. Last" name format.
    """
    name_pattern = re.compile(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$')
    if not name_pattern.match(value):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')

def validate_school_email(value):
    """
    Validator for the school email format ending with "@school.com".
    """
    email_pattern = re.compile(r'^.+@school\.com$')
    if not email_pattern.match(value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_combination_format(value):
    """
    Validator for the format "12-12-12" (ensures there are numbers only).
    """
    combination_pattern = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    if not combination_pattern.match(value):
        raise ValidationError('Combination must be in the format "12-12-12"')

def validate_subject_format(value):
    if type(value)==str and value.istitle():
        return value
    else:
        raise ValidationError('Subject must be a string in title format!')

def validate_professor_name(value):
    professor_pattern = re.compile(r'Professor [A-z][a-z]+')
    if not professor_pattern.match(value):
        raise ValidationError('Professor name must be in the format "Professor Adam"')