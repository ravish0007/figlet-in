import os

from extract_unicode_in import valid_codes
from generate_image import generate_char

os.makedirs('fonts', exist_ok=True)


for code in valid_codes():
    generate_char(code, directory='fonts')
