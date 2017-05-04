"""

http://effbot.org/zone/python-with-statement.htm

http://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

https://www.python.org/dev/peps/pep-0343/

"""
myList = []
with open('n0012.txt', 'r') as f:   # open(name, mode); mode: 'r' read, 'w' write, 'a' append
    for line in f:
        print(line)
