import os
import sys

cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = cur_path.split('src')[0]
os.chdir(root_path)
sys.path.append(root_path + 'src')
print(f'Root path = {root_path}')
