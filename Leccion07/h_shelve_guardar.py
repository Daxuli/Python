import shelve

s = shelve.open('filenames/fileShelve.db')  # crea tres archivos: .bak, .dat, .dir
try:
    var = {'int': 10, 'float': 9.5, 'string': 'Sample data'}  # un diccionario
    s['key1'] = var  # a la llave 'key1' de fileshelce se le asigna var
    s['key2'] = 'un string'
finally:
    s.close()
