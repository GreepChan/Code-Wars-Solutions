import re
def namelist(names):
    tmp = ', '.join([value['name'] for value in names])
    return re.sub(r'(.*), ',r'\1 & ',tmp)
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
