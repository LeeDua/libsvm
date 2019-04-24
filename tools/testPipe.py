
import sys
import os
from subprocess import *


#out = call(['python', 'grid.py','data.txt.scale'])
out = check_output(['python','grid.py','data.txt.scale'])
print("this is the return result from grid")
print(out)
