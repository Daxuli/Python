"""
Attribute types
see also:
https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python
"""
import time


class Safe:
    def __init__(self, secret, pin):  # secured
        self.secret = secret  # public
        self._secret = self.secret  # protected
        self.__PIN = pin  # private

    def get_password(self):
        return self.__PIN

    def change_password(self, pin):
        self.__PIN = pin


mySafe = Safe("he prefers FORTRAN", "0000")

# Accessing/Modifying public variables: OK
print(mySafe.secret)
mySafe.secret = "he prefers MATLAB"
print(mySafe.secret)
print("-----")
# Accessing/Modifying protected variables: can be done but not a good practice
print(mySafe._secret)
mySafe._secret = "using NOTEPAD"
print(mySafe._secret)
print("-----")
# Accessing/Modifying private variables: can't be done outside the class
print(mySafe.get_password())
mySafe.change_password("1234")
print(mySafe.get_password())
mySafe._Safe__PIN = ("9999")  # could be modified/accessed this way, but the variable is private for a reason
print(mySafe._Safe__PIN)

time.sleep(1)
print(mySafe.__PIN)  # trying to access it directly will trigger an error
