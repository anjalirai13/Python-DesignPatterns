from functools import wraps


def make_bold(function):
    """ Decorator Class"""
    @wraps(function)

    #Inner Function
    def print_hello():
        """ Inner Function"""
        statement = function()
        print "<b> " + statement + " </b>"

    return print_hello


@make_bold
def hello_world():
    """Original Function """

    return "Hello World"

hello_world()
print(hello_world.__name__)
print(hello_world.__doc__)