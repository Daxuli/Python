from collections import OrderedDict

CACHE = OrderedDict()
MAX_SIZE = 100

def set_key(key, value):
    "Set a key value, removing oldest key if MAX_SIZE exceeded"
    CACHE[key] = value
    if len(CACHE) > MAX_SIZE:
        CACHE.popitem(last=False)

def get_key(key):
    "Retrieve a key value from the cache, or None if not found"
    return CACHE.get(key, None)

