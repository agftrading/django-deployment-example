from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string.
    """
    return value.replace(arg,'')

# register.filter('cut',cut) # The first one is the string, the second one is the function itself...

# It is also possible to use decorators!...
# as per the example above!!!...
