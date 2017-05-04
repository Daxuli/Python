"""
http://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python

http://www.diveintopython3.net/serializing.html

http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.save.html


Pickle, Marshal, Shelve

Json,...
http://stackoverflow.com/questions/2259270/pickle-or-json
http://www.benfrederickson.com/dont-pickle-your-data/

"""

import pickle

with open('filenames/filenamePickle', 'wb') as f:  # write binary
    var = {1: 'a', 2: 'b'}
    pickle.dump(var, f)

    var1 = [1, 2, 3, 4]
    pickle.dump(var1, f)  # en realidad no esta guardando esto
