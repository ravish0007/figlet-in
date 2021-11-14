import os

text = ' '.join(open('text.txt').read().splitlines())
os.system(f'python3 banner.py {text}')
