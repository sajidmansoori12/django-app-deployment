from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """ This is a custom function made by sajid which cuts out all the values
    of "arg" from the string !
    """
    return value.replace(arg,'')


# register.filter('cut',cut) #Register our function the first param is what we'll call the function,second param is actual call to the function
# The alternative of above line is to use the decorator