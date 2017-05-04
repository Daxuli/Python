import shelve

s = shelve.open('filenames/fileShelve.db')
try:
    for key, value in s.items():
        print("%s|%s|%s" % (key, value, s[key]))

finally:
    s.close()
