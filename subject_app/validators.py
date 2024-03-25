
from django.core.exceptions import ValidationError
import re
def validate_subject_format(value):
    if type(value)==str and value.istitle():
        return value
    else:
        raise ValidationError('Subject must be a string in title format!')

def validate_professor_name(value):
    professor_pattern = re.compile(r'Professor [A-z][a-z]+')
    if not professor_pattern.match(value):
        raise ValidationError('Professor name must be in the format "Professor Adam"')