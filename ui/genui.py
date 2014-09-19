import os
from subprocess import call

files = os.listdir('.')

for file in files:
    if '.ui' in file:
        name = os.path.splitext(file)[0]
        call(['c:\Python33\Scripts\pyside-uic', file, '-o', '../' + name + '.py'])
