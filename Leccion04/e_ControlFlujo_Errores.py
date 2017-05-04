"""
Manejo y control de Errores
"""
def divide(x, y):
    print("%s/%s" %(x, y), end= ": ")
    try:
        result = x / y
    except TypeError:
        """cuando se de un error de tipo entro en esta parte"""
        print("Estas dividiendo un string por un numero")
    except ZeroDivisionError:
        #  raise ZeroDivisionError  # Con raise mando que salte el error
        print("division by zero!")
    else:
        """Esta parte la ejecuta si no ha habido error"""
        print("result is", result)
    finally:
        print("esta parte la ejecuta falle o no")

divide(2, 1)
print("--------------------------------")
divide("2", "1")
print("--------------------------------")
divide(2, 0)


"""
Los errores son una clase y puedo predefinir mi propio tipo de error

copiado de https://docs.python.org/3/tutorial/errors.html
"""
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message