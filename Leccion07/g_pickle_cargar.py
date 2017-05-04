import pickle

"""
w:write
r:read
a:append
"""
with open('filenames/filenamePickle', 'rb') as f:
    var2 = pickle.load(f)

print(var2)